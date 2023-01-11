import networkx as nx
import matplotlib.pyplot as plt


class WeightedGraph(object):
    def __init__(self):
        self.weighted_graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.weighted_graph:
            self.weighted_graph[vertex] = []
        else:
            print(f'Vertex {vertex} is already present')

    def add_edge(self, starting_vertex, ending_vertex, weight):
        if self.verify_vertices(vertices=[starting_vertex, ending_vertex]):
            staring_vertex_edges = self.weighted_graph.get(starting_vertex, [])
            if ending_vertex in staring_vertex_edges:
                print(f'Edge from {starting_vertex} to {ending_vertex} is already present')
            else:
                staring_vertex_edges.append([ending_vertex, weight])
                self.weighted_graph[starting_vertex] = staring_vertex_edges

    def delete_edge(self, starting_vertex, ending_vertex):
        if self.verify_vertices(vertices=[starting_vertex, ending_vertex]):
            staring_vertex_edges = self.weighted_graph.get(starting_vertex, [])
            if ending_vertex not in staring_vertex_edges:
                print(f'Edge from {starting_vertex} to {ending_vertex} is not present')
            else:
                for index, edge in enumerate(staring_vertex_edges):
                    if ending_vertex in edge:
                        staring_vertex_edges.pop(index)
                self.weighted_graph[starting_vertex] = staring_vertex_edges

    def delete_vertex(self, vertex):
        if vertex not in self.weighted_graph:
            print(f'Vertex {vertex} is not present in graph')
        else:
            del self.weighted_graph[vertex]

    def verify_vertices(self, vertices: list) -> bool:
        for vertex in vertices:
            if vertex not in self.weighted_graph:
                print(f'Vertex {vertex} is not present in graph')
                return False
        return True

    def display(self):
        print(self.weighted_graph)
        _graph = nx.DiGraph()
        graph_edges = self.get_graph_edges()
        for graph_edge in graph_edges:
            _graph.add_edge(graph_edge[0], graph_edge[1], weight=graph_edge[2])

        edge_labels = nx.get_edge_attributes(_graph, "weight")
        pos = nx.spring_layout(_graph, seed=7)

        # vertices
        nx.draw_networkx_nodes(_graph, pos, node_size=700, label="ciudades")
        nx.draw_networkx_labels(_graph, pos, font_size=20, font_family="sans-serif")

        # edges
        nx.draw_networkx_edges(
            _graph, pos, width=2, alpha=0.5, edge_color="green", arrowstyle='-|>'
        )
        nx.draw_networkx_edge_labels(_graph, pos, edge_labels)

        plt.show()
        plt.savefig("mygraph.png")

    def get_graph_edges(self) -> list:
        graph_edges = []
        for vertex, edges in self.weighted_graph.items():
            for edge in edges:
                graph_edges.append([vertex, edge[0], edge[1]])
        return graph_edges

    def get_adjacency_matrix(self) -> list:
        graph_vertices = len(self.weighted_graph.keys())
        graph_vertices_integer_map = {}
        counter = 0
        for vertex in self.weighted_graph.keys():
            graph_vertices_integer_map[vertex] = counter
            counter += 1

        adjacency_matrix = [[float('INF') for _ in range(graph_vertices)] for _ in range(graph_vertices)]

        for vertex, integer_no in graph_vertices_integer_map.items():
            adjacency_matrix[integer_no][integer_no] = 0  # self edge
            for edge in self.weighted_graph.get(vertex):
                edge_vertex = edge[0]
                edge_weight = edge[1]
                edge_vertex_integer_no = graph_vertices_integer_map.get(edge_vertex)
                adjacency_matrix[integer_no][edge_vertex_integer_no] = edge_weight

        return adjacency_matrix


if __name__ == '__main__':
    graph = WeightedGraph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')
    graph.add_vertex('g')
    graph.add_vertex('h')

    graph.add_edge(starting_vertex='a', ending_vertex='c', weight=5)
    graph.add_edge(starting_vertex='c', ending_vertex='h', weight=10)
    graph.add_edge(starting_vertex='d', ending_vertex='e', weight=8)
    graph.add_edge(starting_vertex='b', ending_vertex='a', weight=11)
    graph.add_edge(starting_vertex='e', ending_vertex='c', weight=17)
    graph.add_edge(starting_vertex='d', ending_vertex='g', weight=90)
    graph.add_edge(starting_vertex='g', ending_vertex='a', weight=22)
    graph.add_edge(starting_vertex='f', ending_vertex='a', weight=43)
    graph.add_edge(starting_vertex='f', ending_vertex='f', weight=78)
    graph.add_edge(starting_vertex='h', ending_vertex='b', weight=67)

    graph.display()

    graph.delete_vertex('f')
    graph.display()
    graph.delete_vertex('z')

    graph.delete_edge(starting_vertex='c', ending_vertex='h')
    graph.display()
