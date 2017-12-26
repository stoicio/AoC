from tqdm import tqdm

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
    for _ in tqdm(xrange(40000000)):
        next_a = next_value(next_a, GEN_A_FACTOR)
        next_b = next_value(next_b, GEN_B_FACTOR)
        if compare(next_a, next_b):
            matches += 1
    return matches


if __name__ == '__main__':
    gen_a_start, gen_b_start = 634, 301
    print solve(gen_a_start, gen_b_start)
