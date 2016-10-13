class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.nodeList = []
        self.edgeList = []

    def addNode(self, node):
        self.nodeList.append(node)

    def addEdge(self, node1, node2, weight):
        self.edgeList.append((node1, node2, weight))     # Edges added as pair of nodes (unordered) with a weight

    def __str__(self):
        string = "Node List:\n"
        for node in self.nodeList:
            string += str(node) + "\n"
        string += "\nEdge List:\n"
        for edge in self.edgeList:
            string += str(edge[0]) + ", " + str(edge[1]) + ": "+ str(edge[2])
        return string

m = Graph()

cities = ["Minneapolis", "Boston", "Denver"]
for city in cities:
    m.addNode(Node(city))

print(m)
