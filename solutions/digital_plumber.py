from collections import defaultdict

GOAL = 0


def is_reachable(graph, target_node, start_node):  # DFS
    stack = [start_node]
    seen_nodes = set()

    while len(stack):
        curr_node = stack.pop()
        seen_nodes.add(curr_node)
        if curr_node == target_node:
            return True
        for child_node in graph[curr_node]:
            if child_node not in seen_nodes:
                stack.append(child_node)
    return False


def solve_part_one(input_file_path):  # Find nodes connected to GOAL directly or indirectly
    graph = defaultdict(list)

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            this_line = line.strip().replace(' ', '')
            this_line = this_line.replace('<->', ',')
            all_nodes = this_line.split(',')
            if all_nodes:
                all_nodes = [int(i) for i in all_nodes]
                graph[all_nodes[0]] = all_nodes[1:]
    connect_to_zero = 0
    for node in graph:
        if is_reachable(graph, GOAL, node):
            connect_to_zero += 1
    return connect_to_zero


if __name__ == '__main__':
    input_file = 'inputs/digital_plumber/test2.txt'
    result = solve_part_one(input_file)
    print 'Nodes connected to', GOAL, result
