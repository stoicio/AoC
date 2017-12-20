# Referecing http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
# and assuming each cell in grid can be represented by 3 pt coordinates

movement_to_postion = {
    'n': (-1, 0, 1),
    's': (1, 0, -1),
    'ne': (-1, 1, 0),
    'se': (0, 1, -1),
    'nw': (0, -1, 1),
    'sw': (1, -1, 0)
}


def solve(input_movements):

    def get_distance(current_pos):
        return max(abs(i) for i in current_pos)

    movements = input_movements.strip().split(',')
    current = [0, 0, 0]
    max_dist, current_dist = 0, 0
    for move in movements:
        current[0] += movement_to_postion[move][0]
        current[1] += movement_to_postion[move][1]
        current[2] += movement_to_postion[move][2]
        current_dist = get_distance(current)
        if max_dist < current_dist:
            max_dist = current_dist
    return current_dist, max_dist
