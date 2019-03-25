
def spin_program(programs, spin_from_idx):
    # pivot_pt = len(programs) - spin_from_idx
    # new_pgms = programs[pivot_pt:]
    # new_pgms.extend(programs[:pivot_pt])
    return programs[-spin_from_idx:] + programs[:-spin_from_idx]


def swap_idx(programs, idx_a, idx_b):
    programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]
    return programs


def swap_program(programs, prog_a, prog_b):
    idx_a = programs.index(prog_a)
    idx_b = programs.index(prog_b)
    return swap_idx(programs, idx_a, idx_b)


def do_dance_steps(programs, steps):
    for step in steps:
        action = step[0]
        args = step[1:]
        if action == 's':
            idx = int(args)
            programs = programs[-idx:] + programs[:-idx]
        elif action == 'x':
            idx_a, idx_b = map(int, args.split('/'))
            programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]
        elif action == 'p':
            pgm_a, pgm_b = args.split('/')
            idx_a = programs.index(pgm_a)
            idx_b = programs.index(pgm_b)
            programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]

    return ''.join(programs)


def get_dance_steps(input_steps_file):
    with open(input_steps_file, 'r') as steps_file:
        input_steps_str = steps_file.readline().strip()
    return input_steps_str.split(',')


def solve_part_one(input_programs, input_steps_file):
    programs = input_programs[:]
    input_steps = get_dance_steps(input_steps_file)
    return do_dance_steps(programs, input_steps)


def solve_part_two(input_programs, input_steps_file):
    input_steps = get_dance_steps(input_steps_file)
    starting_config = current_config = ''.join(input_programs)

    seen_configs = list()
    seen_configs.append(starting_config)

    for i in xrange(1000000000):
        current_config = do_dance_steps(list(current_config), input_steps)
        if current_config in seen_configs:
            return seen_configs[1000000000 % (i + 1)]
            break
        seen_configs.append(current_config)
