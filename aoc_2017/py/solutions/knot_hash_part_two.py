import functools


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


def get_sparse_hash(knot_lengths):
    arr = range(0, 256)
    current_position = 0
    skip = 0
    for _ in range(0, 64):
        for length in knot_lengths:
            arr = reverse_sub_list(arr, current_position, current_position + length - 1)
            current_position = (current_position + length + skip) % len(arr)
            skip += 1
    return arr


def get_dense_hash(sparse_hash):

    def xor(x, y):
        return x ^ y

    dense_hash = []
    curr_idx_sparse = 0
    while curr_idx_sparse < len(sparse_hash):
        dense_hash.append(functools.reduce(xor, sparse_hash[curr_idx_sparse: curr_idx_sparse + 16]))
        curr_idx_sparse += 16
    return dense_hash


def solve(input_stream):
    input_ascii = [ord(ch) for ch in input_stream]
    input_ascii.extend([17, 31, 73, 47, 23])
    sparse_hash = get_sparse_hash(input_ascii)
    dense_hash = get_dense_hash(sparse_hash)
    hexes = []
    for i in dense_hash:
        hex_val = hex(i)[2:]
        if len(hex_val) < 2:
            hex_val = '0' + hex_val
        hexes.append(hex_val)
    return ''.join(hexes)


if __name__ == '__main__':
    input_str = '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118'
    print 'Knot Hash', solve(input_str)
