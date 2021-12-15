class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = {}

    def add_edge(self, node1, node2):
        for n in (node1, node2):
            if n not in self.nodes:
                self.nodes[n] = []

        self.nodes.get(node1).append(node2)
        self.nodes.get(node2).append(node1)     

    def is_big(self, node):
        return node.isupper()

    def prob1_search(self, current, visited):   
        total = 0

        if current == 'end':
            return 1

        for adj_node in self.nodes.get(current):
            if adj_node not in visited or self.is_big(adj_node):
                total += self.prob1_search(adj_node, visited | {adj_node})

        return total

    def prob2_search(self, current, visited, visit_twice=True):   
        total = 0

        if current == 'end':
            return 1

        for adj_node in self.nodes.get(current):
            if adj_node not in visited or self.is_big(adj_node):
                total += self.prob2_search(adj_node, visited | {adj_node}, visit_twice)
            elif visit_twice and adj_node != 'start' and adj_node != 'end':
                total += self.prob2_search(adj_node, visited | {adj_node}, False)

        return total

def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip().split('-'))

    cave_system = Graph(len(input_array))
    for path in input_array:
        cave_system.add_edge(path[0], path[1])

    return cave_system.prob1_search('start', {'start'})

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(line.strip().split('-'))

    cave_system = Graph(len(input_array))
    for path in input_array:
        cave_system.add_edge(path[0], path[1])

    return cave_system.prob2_search('start', {'start'})