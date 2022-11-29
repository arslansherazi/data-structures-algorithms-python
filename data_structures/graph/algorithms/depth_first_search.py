from data_structures.graph.graph import Graph
from data_structures.stack.stack import Stack


class DepthFirstSearch(object):
    def __init__(self, _graph):
        self.graph = _graph
        self.stack = Stack()
        self.visited_vertices = []

    def depth_first_search(self):
        starting_vertex = list(self.graph.graph.keys())[0]
        self.handle_visited_vertex(starting_vertex)
        _dfs = []
        while starting_vertex:
            adjacent_vertex = self.graph.graph.get(starting_vertex)[0]
            if adjacent_vertex in self.visited_vertices:
                unvisited_vertex_found = False
                for _adjacent_vertex in self.graph.graph.get(starting_vertex):
                    if _adjacent_vertex not in self.visited_vertices:
                        unvisited_vertex_found = True
                        adjacent_vertex = _adjacent_vertex
                        self.handle_visited_vertex(adjacent_vertex)
                        break
                if not unvisited_vertex_found:
                    _dfs.append(self.stack.pop())
                    starting_vertex = self.stack.peek()
                    continue
            else:
                self.handle_visited_vertex(adjacent_vertex)
            starting_vertex = adjacent_vertex
        while True:
            if self.stack.is_empty():
                break
            _dfs.append(self.stack.pop())
        for vertex in _dfs:
            print(vertex, end='\t')

    def handle_visited_vertex(self, vertex):
        self.stack.push(vertex)
        self.visited_vertices.append(vertex)


if __name__ == '__main__':
    graph = Graph()
    dfs = DepthFirstSearch(graph)

    graph.add_vertex('S')
    graph.add_vertex('A')
    graph.add_vertex('D')
    graph.add_vertex('B')
    graph.add_vertex('C')

    graph.add_edge(starting_vertex='S', ending_vertex='A')
    graph.add_edge(starting_vertex='A', ending_vertex='D')
    graph.add_edge(starting_vertex='D', ending_vertex='B')
    graph.add_edge(starting_vertex='B', ending_vertex='S')
    graph.add_edge(starting_vertex='D', ending_vertex='C')
    graph.add_edge(starting_vertex='C', ending_vertex='S')

    dfs.depth_first_search()
