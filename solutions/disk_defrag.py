from math import log

import knot_hash_part_two


def get_ones_in_row(hast_str_for_row):
    hex_hash = knot_hash_part_two.solve(hast_str_for_row)
    base = 16  # hexadecimal
    number_of_bits = len(hex_hash) * log(base, 2)  # calc number of bit to use zfill
    bin_str = bin(int(hex_hash, base))[2:]  # remove 0b from the string
    # if the first number has leading zeros, bin doesn't add them. use zfill
    bin_str = bin_str.zfill(int(number_of_bits))

    return bin_str.count('1')


def solve_part_one(input_hash_str):
    sum = 0
    hash_template = '{input_str}-{row_number}'
    for i in range(128):
        sum += get_ones_in_row(hash_template.format(input_str=input_hash_str, row_number=str(i)))
    return sum


if __name__ == '__main__':
    print 'Number of Used Cells: ', solve_part_one('uugsqrei')
