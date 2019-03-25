from math import log

import knot_hash_part_two


def get_num_connected_components(all_nodes_in_grid):  # BFS
    connected_regions = 0
    while all_nodes_in_grid:
        item = all_nodes_in_grid.pop()
        queue = [item]
        all_nodes_in_grid.add(item)
        while queue:
            # print queue
            row, col = queue.pop()
            if (row, col) in all_nodes_in_grid:  # if this node is a used one
                all_nodes_in_grid.remove((row, col))  # this node is consumed. Remove it
                queue.extend([(row, col + 1), (row - 1, col), (row, col - 1), (row + 1, col)])
        # At this point, all the nodes adjacent to the startin node in queue should
        # be visited and accounted for. This collection of nodes form a region
        connected_regions += 1
    return connected_regions


def get_row_in_binary(hast_str_for_row):
    hex_hash = knot_hash_part_two.solve(hast_str_for_row)
    base = 16  # hexadecimal
    number_of_bits = len(hex_hash) * log(base, 2)  # calc number of bit to use zfill
    bin_str = bin(int(hex_hash, base))[2:]  # remove 0b from the string
    # if the first number has leading zeros, bin doesn't add them. use zfill
    bin_str = bin_str.zfill(int(number_of_bits))
    return bin_str


def solve(input_hash_str):
    hash_template = '{input_str}-{row_number}'
    coordinates_of_used_cells = set()
    for row in range(128):
        bin_row = get_row_in_binary(hash_template.format(input_str=input_hash_str,
                                                         row_number=str(row)))
        coordinates_of_used_cells.update([(row, col) for col, value in enumerate(bin_row) if value == '1'])  # noqa
    used_count = len(coordinates_of_used_cells)
    regions_count = get_num_connected_components(coordinates_of_used_cells)
    return used_count, regions_count


if __name__ == '__main__':
    used_count, regions_count = solve('uugsqrei')
    print 'Number of Used Cells: ', used_count, 'Number of regions: ', regions_count
