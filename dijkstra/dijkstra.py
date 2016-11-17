class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodeList = []
        self.edgeList = []

    def add_node(self, node):
        self.nodeList.append(node)

    def add_edge(self, node1, node2, weight):
        self.edgeList.append((node1, node2, weight))     # Edges added as pair of nodes (unordered) with a weight

    def __str__(self):
        string = "Node List:\n"
        for node in self.nodeList:
            string += str(node) + "\n"
        string += "\nEdge List:\n"
        for edge in self.edgeList:
            string += str(edge[0]) + ", " + str(edge[1]) + ": "+ str(edge[2])
        return string

map = Graph()

distances = ["Minneapolis", "Boston", "Denver"]
for city in cities:
    map.add_node(Node(city))

print(map)
