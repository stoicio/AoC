def parse_input(input_file_path):
    firewall = []

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            this_line = line.strip().replace(' ', '')
            if this_line:
                layer, depth = (int(i) for i in this_line.split(':'))
                firewall.append((layer, depth))
    return firewall


# def move_scanner_for_next_tick(firewall):
# This still works, but is horribly inefficient, the position of the scanner
# in a layer at any point can be calculated by layer_idx  % 2 * (depth - 1)

#     for layer in firewall:
#         depth, position, direction = (layer['depth'], layer['scanner_pos'],
#                                       layer['scanner_direction'])
#         if depth:  # if layer has a depth for scanner to prowl
#             position += 1 * direction
#             if position < 0 or position == depth:
#                 direction *= -1  # reverse the direction
#                  # move the scanner to the right pos
#                 position = (position + (2 * direction)) % depth
#             layer['depth'], layer['scanner_pos'], layer['scanner_direction'] = (depth, position,
#                                                                                 direction)


# def solve_part_one(input_file_path):  # Find nodes connected to GOAL directly or indirectly
#     firewall = parse_input(input_file_path)
#     severity = 0
#     for curr_layer_idx in range(len(firewall)):  # moves self forward through layer
#         curr_layer = firewall[curr_layer_idx]
#         if curr_layer['depth'] != 0 and curr_layer['scanner_pos'] == 0:
#             print "Caught in layer ", curr_layer_idx
#             severity = severity + curr_layer_idx * curr_layer['depth']
#         move_scanner_for_next_tick(firewall)  # moves scanner back or forth in layer
#     return severity

def solve_part_one(input_file_path):
    firewall = parse_input(input_file_path)
    severity = 0
    for layer, depth in firewall:
        scanner_pos = 2 * (depth - 1)
        if layer % scanner_pos == 0:
            severity += depth * layer
    return severity


def solve_part_two(input_file_path):
    firewall = parse_input(input_file_path)
    is_caught = False
    delay = 0
    while True:
        is_caught = False
        delay += 1
        for layer, depth in firewall:
            # It would take 2 * (depth - 1) steps for the scanner to go the depth of the layer
            # and come back up to top of the layer.
            scanner_cycle_length = 2 * (depth - 1)
            # if the scanner pos to go up / down is a even divisor for the layer then it would mean
            # that the scanner would be at the top of layer.
            # layer + delay => Would effectively mean the postion of the scanner at that step.
            if (layer + delay) % scanner_cycle_length == 0:
                is_caught = True
                break
        if not is_caught:
            break
    return delay


if __name__ == '__main__':
    input_file = 'inputs/packet_scanner/test2.txt'
    severity = solve_part_one(input_file)
    print 'Severity of getting caught', severity
    steps_delayed = solve_part_two(input_file)
    print 'Steps to skip to avoid getting caught', steps_delayed
