
def solve(current_state):

    states_seen = {}
    cycles_count = 0
    loop_count = 1  # Account for the state already in the stack
    num_banks = len(current_state)
    states_stack = []  # to backtrack to find the number of cycles taken for repetition
    while True:
        stringified_state = ''.join([str(i) for i in current_state])
        # If we have already seen this state
        if stringified_state in states_seen:
            # Keep popping elements in stack, till we find the goal state
            while states_stack.pop() != stringified_state:
                loop_count += 1
            break
        # Add the new state to dict & to the stack
        states_seen[stringified_state] = 1
        states_stack.append(stringified_state)

        # Find the block with maximum element & index of the block
        max_item = max(current_state)
        max_idx = current_state.index(max_item)
        # Take all the elements from that block and reallocate to all blocks
        current_state[max_idx] = 0
        next_idx = (max_idx + 1) % num_banks
        while max_item > 0:
            current_state[next_idx] += 1
            max_item -= 1
            next_idx = (next_idx + 1) % num_banks
        # Cycles taken to get to a state that was already seen before
        cycles_count += 1
    return cycles_count, loop_count


if __name__ == '__main__':
    result = solve([11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11])
    print 'Number of Total Cycles :', result[0]
    print 'Number of redistrubution cycles after detecting a previous state : ', result[1]
