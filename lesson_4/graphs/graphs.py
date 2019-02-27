class Edge():
    def __init__(self, weight, node_a=None, node_b=None):
        self.weight = weight
        self.node_a = node_a
        self.node_b = node_b

    def nodes(self):
        return (self.node_a, self.node_a)


class Node():
    def __init__(self, key):
        self.key = key

    def linked_nodes(self, edges):
        nodes = [edge.nodes()[1] for edge in edges if edge.nodes()[0] == self]
        nodes += [edge.nodes()[0] for edge in edges if edge.nodes()[1] == self]
        return nodes


class Graph():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def __contains__(self, node):
        return node in self.nodes

    def __iter__(self):
        return iter(self.nodes)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
        else:
            print "Node is already in graph"

    def remove_node(self, node):
        self.edges = filter(lambda edge: node not in edge.nodes(), self.edges)
        self.nodes.remove(node)

    def add_egde(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

    def shortest_path(self, node_a, node_b):
        pass


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    edges = [
        Edge(1, node1, node2),
        Edge(2, node2, node3),
        Edge(2, node3, node1),
        Edge(0.5, node1, node3)
        ]
    print node1.linked_nodes(edges)

    g = Graph([node1, node3], [edges[0]])
    g.add_node(node2)
    g.add_egde(edges[1])
    g.add_egde(edges[2])
    g.add_egde(edges[3])