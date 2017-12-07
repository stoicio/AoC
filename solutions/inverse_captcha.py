# --- Day 1: Inverse Captcha ---
#
# Problem Statement :
# For example: http://adventofcode.com/2017/day/1
#
#  1122 produces a sum of 3 (1 + 2)
#   - because the first digit (1) matches the second digit
#     and the third digit (2) matches the fourth digit.
#  1111 produces 4
#   - because each digit (all 1) matches the next.
#  1234 produces 0 because no digit matches the next.
#  91212129 produces 9 because
#   - the only digit that matches the next one is the last digit, 9.
#
# What is the solution to your captcha?

import sys


def _convert_str_to_digits(input_str):
    '''Given a string of digits, transform them into a list of single digit ints'''
    return map(lambda x: int(x), list(input_str))


def solve(input_str, step_size):
    digits = _convert_str_to_digits(input_str)
    num_digits = len(digits)
    # step = num_digits // 2
    final_sum = 0
    for curr_idx in xrange(num_digits):
        idx_to_compare = (curr_idx + step_size) % num_digits
        if digits[curr_idx] == digits[idx_to_compare]:
            final_sum += digits[curr_idx]
    return final_sum


if __name__ == '__main__':
    input_string = ''
    result = 0
    part_one_result = 1034
    part_two_result = 1356
    step_size = 0
    if len(sys.argv) == 1:
        print "Run step one or two ? Usage : python -m solutions.inverse_captcha <one|two>"
        sys.exit(0)
    with open('inputs/inverse_captcha.txt', 'r') as input_file:
        input_string = input_file.readline().replace('\n', '')

    if sys.argv[1] == 'one':
        step_size = 1
    elif sys.argv[1] == 'two':
        step_size = len(input_string) // 2

    result = solve(input_string, step_size)
    print 'Result is', result
