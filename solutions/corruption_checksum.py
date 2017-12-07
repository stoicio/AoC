# --- Day 2: Corruption Checksum ---
# For example, given the following spreadsheet:
#
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
#
# - In the first row, the only two numbers that evenly divide are 8 and 2; t
#   he result of this division is 4.
# - In the second row, the two numbers are 9 and 3; the result is 3.
# - In the third row, the result is 2.
#
# In this example, the sum of the results would be 4 + 3 + 2 = 9.
#
# What is the sum of each row's result in your puzzle input?

import sys


def solve(input_file_path, part='one'):
    checksum = 0
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            # remove leading and trailing whitespace chars
            stripped_line = line.strip()
            # convert all numbers to int
            all_digits = map(lambda x: int(x), stripped_line.split())
            if all_digits and part == 'one':  # diff of min and max in row
                min_in_line, max_in_line = min(all_digits), max(all_digits)
                checksum += max_in_line - min_in_line
            elif all_digits and part == 'two':  # Sum of result of evenly divisible numbers in row
                for i in range(len(all_digits)):
                    for j in range(len(all_digits)):
                        if i != j and all_digits[i] % all_digits[j] == 0:
                            checksum += all_digits[i] // all_digits[j]
    return checksum


if __name__ == '__main__':
    input_file_path = './inputs/corruption_checksum/test2.txt'
    result = 0

    if len(sys.argv) < 2 or (sys.argv[1] != 'one' and sys.argv[1] != 'two'):
        print "Run step one or two ? Usage : python -m solutions.corruption_checksum <one|two>"
        sys.exit(0)

    result = solve(input_file_path, sys.argv[1])
    print 'Result is', result
