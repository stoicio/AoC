def reverse_sub_list(arr, start, end):
    b = arr[:]

    while start < end:
        start_idx, end_idx = start, end
        if start >= len(arr):
            start_idx = start % len(arr)
        if end >= len(arr):
            end_idx = end % len(arr)
        b[start_idx], b[end_idx] = b[end_idx], b[start_idx]
        start += 1
        end -= 1
    return b


def solve(knot_lengths):
    arr = range(0, 256)
    current_position = 0
    skip = 0
    for length in knot_lengths:
        arr = reverse_sub_list(arr, current_position, current_position + length - 1)
        current_position = (current_position + length + skip) % len(arr)
        skip += 1
    return arr[0] * arr[1]


if __name__ == '__main__':
    input_lengths = [106, 118, 236, 1, 130, 0, 235, 254, 59, 205, 2, 87, 129, 25, 255, 118]
    print "Result", solve(input_lengths)
