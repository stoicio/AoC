from collections import defaultdict
from Queue import Queue
import threading


def get_input(file_path):
    instructions = []
    with open(file_path, 'r') as data_file:
        for line in data_file:
            line = line.strip()
            if line:
                split_line = line.split()
                instruction = split_line[0]
                register = split_line[1]
                value = None
                if len(split_line) > 2:
                    value = split_line[2]
                instructions.append({'cmd': instruction, 'reg': register, 'val': value})
    return instructions


def get_val(registers, value):
    if value in 'abcdefghijklmnopqrstuvwxyz':
        return registers[value]
    else:
        return int(value)


def solve_part_one(file_path):
    input_data = get_input(file_path)
    last_played_freq = None
    curr_instr_idx = 0
    registers = defaultdict(int)

    while curr_instr_idx >= 0 and curr_instr_idx < len(input_data):
        jump = False
        curr_instr = input_data[curr_instr_idx]
        value = get_val(registers, curr_instr['val']) if curr_instr['val'] else None
        if curr_instr['cmd'] == 'snd':
            last_played_freq = registers[curr_instr['reg']]
        elif curr_instr['cmd'] == 'set':
            registers[curr_instr['reg']] = value
        elif curr_instr['cmd'] == 'add':
            registers[curr_instr['reg']] += value
        elif curr_instr['cmd'] == 'mul':
            registers[curr_instr['reg']] *= value
        elif curr_instr['cmd'] == 'mod':
            registers[curr_instr['reg']] %= value
        elif curr_instr['cmd'] == 'jgz' and registers[curr_instr['reg']] != 0:
            jump = True
            curr_instr_idx += value
        elif curr_instr['cmd'] == 'rcv' and registers[curr_instr['reg']] != 0:
            break
        if not jump:
            curr_instr_idx += 1

    return last_played_freq


class Processor(threading.Thread):
    def __init__(self, pid, rx_queue, send_queue, input_data):
        super(Processor, self).__init__()
        self.rx_queue = rx_queue
        self.send_queue = send_queue
        self.pid = pid
        self.input_data = input_data

    def run(self):
        curr_instr_idx = 0
        registers = defaultdict(int)
        registers['p'] = self.pid
        send_count = 0

        while curr_instr_idx >= 0 and curr_instr_idx < len(self.input_data):
            jump = False
            curr_instr = self.input_data[curr_instr_idx]
            value = get_val(registers, curr_instr['val']) if curr_instr['val'] else None

            if curr_instr['cmd'] == 'set':
                registers[curr_instr['reg']] = value
            elif curr_instr['cmd'] == 'add':
                registers[curr_instr['reg']] += value
            elif curr_instr['cmd'] == 'mul':
                registers[curr_instr['reg']] *= value
            elif curr_instr['cmd'] == 'mod':
                registers[curr_instr['reg']] %= value
            elif curr_instr['cmd'] == 'jgz' and get_val(registers, curr_instr['reg']) != 0:
                jump = True
                curr_instr_idx += value

            if curr_instr['cmd'] == 'snd':
                send_count += 1
                self.send_queue.put(value)
            elif curr_instr['cmd'] == 'rcv':
                try:
                    rx_value = self.rx_queue.get(timeout=5)
                    registers[curr_instr['reg']] = rx_value
                    self.rx_queue.task_done()
                except Exception:
                    print 'Program', self.pid, 'Ran out of values'
                    break

            if not jump:
                curr_instr_idx += 1

        print 'Program ', self.pid, ' send count ', send_count


def solve_part_two(file_path):

    input_data = get_input(file_path)

    pid_1 = 0
    pid_2 = 1

    program_1_queue = Queue(32)
    program_2_queue = Queue(32)

    program_1 = Processor(pid_1, program_1_queue, program_2_queue, input_data)
    program_2 = Processor(pid_2, program_2_queue, program_1_queue, input_data)

    program_1.start()
    program_2.start()

    program_1_queue.join()
    program_2_queue.join()
