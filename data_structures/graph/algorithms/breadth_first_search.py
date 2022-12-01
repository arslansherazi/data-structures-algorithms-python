from data_structures.graph.graph import Graph
from data_structures.queue.queue import Queue


class BreadthFirstSearch(object):
    def __init__(self, _graph):
        self.graph = _graph
        self.queue = Queue(size=10000)
        self.visited_vertices = set()
        self.starting_vertex = list(self.graph.weighted_graph.keys())[0]

    def breadth_first_search(self):
        self.queue.enqueue(self.starting_vertex)
        while not self.queue.is_empty():
            next_vertex = self.queue.dequeue()
            self.visited_vertices.add(next_vertex)
            print(next_vertex, end='\t')
            for adjacent_vertex in self.graph.weighted_graph.get(next_vertex):
                if adjacent_vertex not in self.visited_vertices:
                    self.queue.enqueue(adjacent_vertex)


if __name__ == '__main__':
    graph = Graph()

    graph.add_vertex('S')
    graph.add_vertex('A')
    graph.add_vertex('D')
    graph.add_vertex('B')
    graph.add_vertex('C')

    graph.add_edge(starting_vertex='S', ending_vertex='A')
    graph.add_edge(starting_vertex='S', ending_vertex='B')
    graph.add_edge(starting_vertex='S', ending_vertex='C')
    graph.add_edge(starting_vertex='A', ending_vertex='D')
    graph.add_edge(starting_vertex='D', ending_vertex='B')
    graph.add_edge(starting_vertex='D', ending_vertex='C')

    graph.display()

    bfs = BreadthFirstSearch(graph)
    bfs.breadth_first_search()
