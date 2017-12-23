def parse_input(input_file_path):
    firewall = []

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            this_line = line.strip().replace(' ', '')
            if this_line:
                layer, depth = [int(i) for i in this_line.split(':')]
                while len(firewall) != layer:
                    firewall.append({'depth': 0, 'scanner_pos': 0, 'scanner_direction': 0})
                firewall.append({'depth': depth, 'scanner_pos': 0, 'scanner_direction': 1})
    return firewall


def move_scanner_for_next_tick(firewall):
    for layer in firewall:
        depth, position, direction = (layer['depth'], layer['scanner_pos'],
                                      layer['scanner_direction'])
        if depth:  # if layer has a depth for scanner to prowl
            position += 1 * direction
            if position < 0 or position == depth:
                direction *= -1  # reverse the direction
                position = (position + (2 * direction)) % depth  # move the scanner to the right pos
            layer['depth'], layer['scanner_pos'], layer['scanner_direction'] = (depth, position,
                                                                                direction)


def solve_part_one(input_file_path):  # Find nodes connected to GOAL directly or indirectly
    firewall = parse_input(input_file_path)
    severity = 0
    for curr_layer_idx in range(len(firewall)):  # moves self forward through layer
        curr_layer = firewall[curr_layer_idx]
        if curr_layer['depth'] != 0 and curr_layer['scanner_pos'] == 0:
            print "Caught in layer ", curr_layer_idx
            severity = severity + curr_layer_idx * curr_layer['depth']
        move_scanner_for_next_tick(firewall)  # moves scanner back or forth in layer
    return severity


if __name__ == '__main__':
    input_file = 'inputs/packet_scanner/test2.txt'
    severity = solve_part_one(input_file)
    print 'Severity of getting caught', severity
