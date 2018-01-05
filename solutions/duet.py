from collections import defaultdict


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
