import networkx as nx
import matplotlib.pyplot as plt


class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f'Vertex {vertex} is already present')

    def add_edge(self, starting_vertex, ending_vertex):
        if self.verify_vertices(vertices=[starting_vertex, ending_vertex]):
            staring_vertex_edges = self.graph.get(starting_vertex, [])
            if ending_vertex in staring_vertex_edges:
                print(f'Edge from {starting_vertex} to {ending_vertex} is already present')
            else:
                staring_vertex_edges.append(ending_vertex)
                self.graph[starting_vertex] = staring_vertex_edges

    def delete_edge(self, starting_vertex, ending_vertex):
        if self.verify_vertices(vertices=[starting_vertex, ending_vertex]):
            staring_vertex_edges = self.graph.get(starting_vertex, [])
            if ending_vertex not in staring_vertex_edges:
                print(f'Edge from {starting_vertex} to {ending_vertex} is not present')
            else:
                staring_vertex_edges.remove(ending_vertex)
                self.graph[starting_vertex] = staring_vertex_edges

    def delete_vertex(self, vertex):
        if vertex not in self.graph:
            print(f'Vertex {vertex} is not present in graph')
        else:
            del self.graph[vertex]

    def verify_vertices(self, vertices: list) -> bool:
        for vertex in vertices:
            if vertex not in self.graph:
                print(f'Vertex {vertex} is not present in graph')
                return False
        return True

    def display(self):
        graph = nx.Graph()
        graph_edges = self.get_adjacency_matrix()
        graph.add_edges_from(graph_edges)
        nx.draw_networkx(graph)
        plt.show()
        plt.savefig("mygraph.png")

    def get_adjacency_matrix(self) -> list:
        graph_edges = []
        for vertex, edges in self.graph.items():
            for edge in edges:
                graph_edges.append([vertex, edge])
        return graph_edges


if __name__ == '__main__':
    graph = Graph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')
    graph.add_vertex('g')
    graph.add_vertex('h')

    graph.add_edge(starting_vertex='a', ending_vertex='c')
    graph.add_edge(starting_vertex='c', ending_vertex='h')
    graph.add_edge(starting_vertex='d', ending_vertex='e')
    graph.add_edge(starting_vertex='b', ending_vertex='a')
    graph.add_edge(starting_vertex='f', ending_vertex='f')
    graph.add_edge(starting_vertex='e', ending_vertex='c')
    graph.add_edge(starting_vertex='d', ending_vertex='g')
    graph.add_edge(starting_vertex='g', ending_vertex='a')
    graph.add_edge(starting_vertex='f', ending_vertex='a')
    graph.add_edge(starting_vertex='h', ending_vertex='b')

    graph.display()

    graph.delete_vertex('f')
    graph.display()
    graph.delete_vertex('z')

    graph.delete_edge(starting_vertex='c', ending_vertex='h')
    graph.display()
