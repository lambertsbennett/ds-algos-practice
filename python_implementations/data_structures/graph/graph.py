class Graph:
    def __init__(self):
        self.num_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, node) -> None:
        self.adjacency_list.setdefault(node, [])
        self.num_nodes += 1

    def add_edge(self, node1, node2) -> None:
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def show_connections(self) -> None:
        for node in self.adjacency_list.keys():
            print(f"{node} -> {' '.join([str(x) for x in self.adjacency_list[node]])}")


if __name__ == "__main__":
    g = Graph()
    for i in range(7):
        g.add_vertex(i)
    g.add_edge(3, 1)
    g.add_edge(3, 4)
    g.add_edge(4, 2)
    g.add_edge(4, 5)
    g.add_edge(1, 2)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(6, 5)
    g.show_connections()
