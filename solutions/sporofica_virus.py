INFECTED = '#'
CLEAN = '.'


def get_state_from_file(input_file_path):
    all_lines = []
    with open(input_file_path) as input_file:
        for line in input_file:
            if line.strip():
                all_lines.append(line.strip())
    total_lines = len(all_lines)
    center = (total_lines / 2, len(all_lines[0]) / 2)  # (row, col) => (x, y)

    infected_nodes = set()
    for row in range(total_lines):
        for col in range(len(all_lines[0])):
            if all_lines[row][col] == '#':
                offset_row = center[0] - row
                offset_col = col - center[1]
                infected_nodes.add((offset_row, offset_col))
    return infected_nodes


def get_next_dir(curr_direction, next_direction):
    row, col = curr_direction[1], curr_direction[0]  # swap row and col

    if next_direction == 'left':
        col *= -1  # if direction is left, flip the sign of col
    else:
        row *= -1  # if direction is right, flip the sign of row
    return (row, col)


def solve_part_one(input_file_path):
    infected_nodes = get_state_from_file(input_file_path)
    curr_node = (0, 0)  # start from center
    curr_dir = (1, 0)   # start facing UP
    infections = 0
    for i in range(0, 10000):
        if curr_node in infected_nodes:
            next_dir = get_next_dir(curr_dir, 'right')
            print 'Step ', i + 1, 'In Infected Node, Cleaning  ', curr_node, 'moving right'
            infected_nodes.remove(curr_node)
            curr_node = (curr_node[0] + next_dir[0], curr_node[1] + next_dir[1])
            curr_dir = next_dir
        else:
            next_dir = get_next_dir(curr_dir, 'left')
            print 'Step ', i + 1, 'In Clean Node   , Infecting ', curr_node, 'moving left'
            infected_nodes.add(curr_node)
            infections += 1
            curr_node = (curr_node[0] + next_dir[0], curr_node[1] + next_dir[1])
            curr_dir = next_dir
    return infections
