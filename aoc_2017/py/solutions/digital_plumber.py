from collections import defaultdict

GOAL = 0


def get_all_connected_nodes(graph, node):
    stack = [node]
    seen_nodes = set()

    while len(stack):
        curr_node = stack.pop()
        seen_nodes.add(curr_node)
        for child_node in graph[curr_node]:
            if child_node not in seen_nodes:
                stack.append(child_node)
    return seen_nodes


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


def make_graph_from_input(input_file_path):
    graph = defaultdict(list)

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            this_line = line.strip().replace(' ', '')
            this_line = this_line.replace('<->', ',')
            all_nodes = this_line.split(',')
            if all_nodes:
                all_nodes = [int(i) for i in all_nodes]
                graph[all_nodes[0]] = all_nodes[1:]
    return graph


def solve_part_one(input_file_path):  # Find nodes connected to GOAL directly or indirectly
    graph = make_graph_from_input(input_file_path)

    num_connected_to_goal = 0
    for node in graph:
        if is_reachable(graph, GOAL, node):
            num_connected_to_goal += 1
    return num_connected_to_goal


def solve_part_two(input_file_path):
    graph = make_graph_from_input(input_file_path)
    connected_components = []

    for node in graph:
        is_already_in_a_group = False
        for group in connected_components:
            if node in group:
                is_already_in_a_group = True
        if not is_already_in_a_group:
            group = get_all_connected_nodes(graph, node)
            connected_components.append(group)
    return len(connected_components)


if __name__ == '__main__':
    input_file = 'inputs/digital_plumber/test2.txt'
    _is_reachable_result = solve_part_one(input_file)
    _connected_component_result = solve_part_one(input_file)
    print 'Nodes connected to', GOAL, _is_reachable_result
    print 'Total number of connected components', _connected_component_result
