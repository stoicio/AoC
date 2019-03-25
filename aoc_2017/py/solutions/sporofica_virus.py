def get_state_from_file(input_file_path):
    all_lines = []
    with open(input_file_path) as input_file:
        for line in input_file:
            if line.strip():
                all_lines.append(line.strip())
    total_lines = len(all_lines)
    center = (total_lines / 2, len(all_lines[0]) / 2)  # (row, col) => (x, y)

    center = center[0] + center[1] * 1j

    infected_nodes = set()
    for row in range(total_lines):
        for col in range(len(all_lines[0])):
            if all_lines[row][col] == '#':
                offset = (center.real - row) + (col - center.imag) * 1j
                infected_nodes.add(offset)
    return infected_nodes


def get_next_dir(curr_direction, next_direction):
    next_dir = 0j
    if next_direction == 'reverse':  # Flip the signs 
        next_dir = curr_direction * -1
    else:
        if next_direction == 'left':
            next_dir = curr_direction * -1j  # if direction is left, multiply by -1j
        else:
            next_dir = curr_direction * 1j  # if direction is right, multiply by 1j
    return next_dir


def solve_part_one(input_file_path):
    infected_nodes = get_state_from_file(input_file_path)
    curr_node = 0 + 0j  # start from center
    curr_dir = 1 + 0j   # start facing UP
    infections = 0
    for i in range(0, 10000):
        next_dir = curr_dir
        if curr_node in infected_nodes:
            next_dir = get_next_dir(curr_dir, 'right')
            infected_nodes.remove(curr_node)
        else:
            next_dir = get_next_dir(curr_dir, 'left')
            infected_nodes.add(curr_node)
            infections += 1
        curr_node = curr_node + next_dir
        curr_dir = next_dir
    return infections


def solve_part_two(input_file_path):
    infected_nodes = get_state_from_file(input_file_path)
    weak_nodes = set()
    flagged_nodes = set()

    curr_node = 0 + 0j  # start from center
    curr_dir = 1 + 0j   # start facing UP

    infections = 0
    for i in xrange(0, 10000000):
        next_dir = curr_dir
        if curr_node in infected_nodes:
            next_dir = get_next_dir(curr_dir, 'right')
            infected_nodes.remove(curr_node)
            flagged_nodes.add(curr_node)
        elif curr_node in weak_nodes:
            # No direction change
            weak_nodes.remove(curr_node)
            infected_nodes.add(curr_node)
            infections += 1
        elif curr_node in flagged_nodes:
            # Reverses Direction
            next_dir = get_next_dir(curr_dir, 'reverse')
            flagged_nodes.remove(curr_node)
        else:  # In Clean node
            next_dir = get_next_dir(curr_dir, 'left')
            weak_nodes.add(curr_node)
        curr_node = curr_node + next_dir
        curr_dir = next_dir
    return infections
