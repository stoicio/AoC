
def solve_part_one(steps):
    num_insertions = 2018
    state_buffer = [0]
    pos = 0
    for i in range(1, num_insertions):
        pos = ((pos + steps) % i) + 1
        state_buffer.insert(pos, i)
    return state_buffer[pos + 1]


def solve_part_two(steps):
    num_insertions = 50000000
    pos = 0
    result = -1
    for i in range(1, num_insertions):
        pos = ((pos + steps) % i) + 1
        if pos == 1: 
            result = i
    return result


def main():
    print solve_part_one(386)
    print solve_part_two(386)


if __name__ == '__main__':
    main()

