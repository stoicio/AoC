GEN_A_FACTOR = 16807
GEN_B_FACTOR = 48271
MODULO = 2147483647


def next_value(curr_value, factor):
    next_value = curr_value * factor
    next_value %= MODULO
    return next_value


def compare(a, b):
    bin_str_a = bin(a)
    bin_str_b = bin(b)
    return bin_str_a[-16:] == bin_str_b[-16:]


def solve(start_a, start_b):
    matches = 0
    next_a = start_a
    next_b = start_b
    for _ in xrange(40000000):
        next_a = next_value(next_a, GEN_A_FACTOR)
        next_b = next_value(next_b, GEN_B_FACTOR)
        if compare(next_a, next_b):
            matches += 1
    return matches


def solve_part_two(start_a, start_b):
    queue_a, queue_b = list(), list()
    next_a = start_a
    next_b = start_b
    while True:
        next_a = next_value(next_a, GEN_A_FACTOR)
        next_b = next_value(next_b, GEN_B_FACTOR)

        if next_a % 4 == 0:
            queue_a.append(next_a)
        if next_b % 8 == 0:
            queue_b.append(next_b)

        if len(queue_a) >= 5000000 and len(queue_b) >= 5000000:
            break

    matches = 0
    for i in xrange(5000000):
        if compare(queue_a[i], queue_b[i]):
            matches += 1
    return matches


if __name__ == '__main__':
    gen_a_start, gen_b_start = 634, 301
    print solve_part_two(gen_a_start, gen_b_start)
