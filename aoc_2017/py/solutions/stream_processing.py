
def solve(input_stream):
    # input_stream = input_stream.replace(',', '')
    curr_idx = 0
    is_in_garbage = False
    curr_score = 0
    total_score = 0
    things_in_garbage = 0

    while curr_idx < len(input_stream):
        ch = input_stream[curr_idx]
        if ch == '!':
            curr_idx += 1  # Ignore this char and the next

        elif is_in_garbage and ch != '>':
            things_in_garbage += 1

        elif ch == '<':
            is_in_garbage = True

        elif is_in_garbage and ch == '>':
            is_in_garbage = False

        elif ch == '{' and not is_in_garbage:
            curr_score += 1
            total_score += curr_score

        elif ch == '}' and not is_in_garbage:
            curr_score -= 1

        curr_idx += 1
    return things_in_garbage, total_score
