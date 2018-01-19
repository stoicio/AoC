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

    if value.isalpha():
        return registers[value]
    else:
        return int(value)


def solve_part_one(file_path):
    input_data = get_input(file_path)
    curr_instr_idx = 0
    mul_count = 0
    registers = defaultdict(int)

    while curr_instr_idx >= 0 and curr_instr_idx < len(input_data):
        jump_val = 1
        curr_instr = input_data[curr_instr_idx]
        value = get_val(registers, curr_instr['val']) if curr_instr['val'] else None

        if curr_instr['cmd'] == 'set':
            registers[curr_instr['reg']] = value
        elif curr_instr['cmd'] == 'sub':
            registers[curr_instr['reg']] -= value
        elif curr_instr['cmd'] == 'mul':
            registers[curr_instr['reg']] *= value
            mul_count += 1
        elif curr_instr['cmd'] == 'jnz' and get_val(registers, curr_instr['reg']) != 0:
            jump_val = value

        curr_instr_idx += jump_val

    return mul_count


def solve_part_two(file_path):
    input_data = get_input(file_path)
    curr_instr_idx = 0
    mul_count = 0
    registers = defaultdict(int)
    registers['a'] = 1
    count = 0
    while curr_instr_idx >= 0 and curr_instr_idx < len(input_data):
        jump_val = 1
        curr_instr = input_data[curr_instr_idx]
        value = get_val(registers, curr_instr['val']) if curr_instr['val'] else None

        if curr_instr['cmd'] == 'set':
            registers[curr_instr['reg']] = value
        elif curr_instr['cmd'] == 'sub':
            registers[curr_instr['reg']] -= value
        elif curr_instr['cmd'] == 'mul':
            registers[curr_instr['reg']] *= value
            mul_count += 1
        elif curr_instr['cmd'] == 'jnz' and get_val(registers, curr_instr['reg']) != 0:
            jump_val = value

        curr_instr_idx += jump_val
        print 'a =', registers['a'], 'b =', registers['b'], 'c =', registers['c'], \
              'd =', registers['d'], 'e =', registers['e'], 'f =', registers['f'], \
              'g =', registers['g'], 'h =', registers['h']
        count += 1
        if count > 20:
            break
    # b and c are constant after first few iterations
    # the assembly code when written down, just counts composite numbers
    # between b and c, jumping 17 after each check

    print registers['b'], registers['c']
    composite_numbers = 0
    for i in range(registers['b'], registers['c'] + 1, 17):
        for j in range(2, int(i ** 0.5)):
            if i % j == 0:
                composite_numbers += 1
                break

    return composite_numbers
