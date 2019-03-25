from os import path
import sys


def solve(input_file_path, step):
    with open(input_file_path, 'r') as input_file:
        jumps = [int(line.strip()) for line in input_file]

        next_jump_idx = 0
        jump_count = 0
        while next_jump_idx < len(jumps):
            jump_count += 1
            next_offset = jumps[next_jump_idx]
            if step == 'two' and next_offset >= 3:
                # If solving for second part and next_offset 3 or more
                jumps[next_jump_idx] -= 1
            else:
                # increment current idx's jump value
                jumps[next_jump_idx] += 1

            # set next jump index
            next_jump_idx = next_jump_idx + next_offset

        return jump_count


if __name__ == '__main__':
    input_file_path = './inputs/maze_twisty_trampoline/test2.txt'
    module_name = path.splitext(path.basename(sys.argv[0]))[0]
    result = 0

    if len(sys.argv) < 2 or (sys.argv[1] != 'one' and sys.argv[1] != 'two'):
        print ("Run step one or two ? "
               "Usage : python -m solutions.{name} <one|two>".format(name=module_name))
        sys.exit(0)

    result = solve(input_file_path, sys.argv[1])

    print 'Result is', result
