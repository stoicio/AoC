from collections import defaultdict


def parse_input_line(input_line):
    tokens = input_line.split()
    this_expr = {
        'register': tokens[0],
        'sign': 1 if tokens[1] == 'inc' else -1,
        'change_val': int(tokens[2]),
        'compare_reg': tokens[4],
        'comparator': tokens[5],
        'compare_amt': tokens[6]
    }
    return this_expr


def solve(input_file_path):
    registers = defaultdict(int)
    max_transition = -1000000
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            exp = parse_input_line(line.strip())

            compare_reg_val = registers[exp['compare_reg']]
            if eval(str(compare_reg_val) + exp['comparator'] + exp['compare_amt']):
                curr_value = registers[exp['register']] + exp['sign'] * exp['change_val']
                registers[exp['register']] = curr_value
                if curr_value > max_transition:
                    max_transition = curr_value

    max_value = max([v for k, v in registers.items()])
    return max_value, max_transition


if __name__ == '__main__':
    input_file_path = './inputs/registers/test2.txt'
    result = solve(input_file_path)
    print 'Max Reg Value', result[0], 'Max Transition Value', result[1]
