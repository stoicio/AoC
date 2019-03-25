import re


class Tree(object):

    def __init__(self):
        self.nodes = {}

    def add_node(self, name, weight, children):
        if name in self.nodes:
            self.nodes[name]['weight'] = int(weight)
            self.nodes[name]['children'] = children
        else:
            self.nodes[name] = {'weight': int(weight), 'children': children}

        for child in children:
            if child in self.nodes:
                self.nodes[child]['parent'] = name
            else:
                self.nodes[child] = {'parent': name}


def parse_input_line(input_line):
    pattern = re.compile("(\w+) \((\d+)\)(?: -> (.+))?")
    tokens = pattern.match(input_line).groups()
    node, weight = tokens[0], tokens[1]
    children = []
    if tokens[2]:
        children = tokens[2].split(',')
        children = [i.strip() for i in children]
    return (node, weight, children)


def get_tree(input_file_path):
    tree = Tree()
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            node, weight, children = parse_input_line(line.strip())
            tree.add_node(node, weight, children)
    return tree


def get_parent(tree):
    for node in tree.nodes:
        if not tree.nodes[node].get('parent', None):
            return node


if __name__ == '__main__':
    input_file_path = './inputs/recursive_circus/test1.txt'
    tree = get_tree(input_file_path)
    parent = get_parent(tree)
    print tree.nodes[parent]['children']
    print 'Parent :', parent
