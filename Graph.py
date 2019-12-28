class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edges = []
        for edge in self.edges:
            edges.append((edge.value, edge.node_from.value, edge.node_to.value))
        return edges

    def get_adjacency_list(self):
        adjacency = []
        max_node = self.nodes[0].value
        for node in self.nodes[1:]:
            if node.value > max_node:
                max_node = node.value
        for i in range(max_node + 1):
            adjacency.append([])
            for edge in self.edges:
                if i == edge.node_from.value:
                    adjacency[i].append((edge.node_to.value, edge.value))
            if not adjacency[i]:
                adjacency[i] = None
        return adjacency

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        matrix = []
        max_node = self.nodes[0].value
        for node in self.nodes[1:]:
            if node.value > max_node:
                max_node = node.value
        for i in range(max_node+1):
            matrix.append([])
            for j in range(max_node+1):
                matrix[i].append(0)
        i, j = 0, 0
        for node in self.nodes:
            for edge in self.edges:
                if node.value == edge.node_from.value:
                    matrix[node.value][edge.node_to.value] = edge.value
        return matrix


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
