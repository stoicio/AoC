NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


def get_maze_from_file(input_file_path):
    maze = []
    with open(input_file_path) as maze_file:
        for line in maze_file:
            if line.strip():
                maze.append(line)
    return maze


def explore_maze(maze):
    collected_items = ''
    curr_direction = SOUTH
    row = 0
    col = maze[0].index('|')
    curr_position = (row, col)
    curr_symbol = '|'
    total_moves = 0
    # print 'Position', 'Row', row, 'Col', col, 'Symbol', maze[row][col]
    # print 'Position', 'Y', row + 1, 'X', col, 'Symbol', maze[row][col]

    while maze[row][col] != ' ':  # Explore till we hit a space or run out of directions
        row, col = (curr_position[0] + curr_direction[0],
                    curr_position[1] + curr_direction[1])
        curr_symbol = maze[row][col]
        total_moves += 1
        # print curr_symbol, ' --> '
        if curr_symbol == '+':  # determine new direction
            if curr_direction == NORTH or curr_direction == SOUTH:  # Travelling along Y
                curr_direction = WEST if maze[row][col - 1] != ' ' else EAST
            else:  # Travelling along X / Check Y for new direction
                curr_direction = NORTH if maze[row - 1][col] != ' ' else SOUTH
        elif curr_symbol != '|' and curr_symbol != '-':
            collected_items += curr_symbol
        curr_position = (row, col)
    return (total_moves, collected_items.strip())


def solve(input_maze_file):
    maze = get_maze_from_file(input_maze_file)
    total_steps, collected_items = explore_maze(maze)
    print 'Total Steps to Exit Maze: ', total_steps, ' Collected Items: ', collected_items
    return (total_steps, collected_items)
