from data_structures.graph.graph import Graph
from data_structures.stack.stack import Queue


class DepthFirstSearch(object):
    def __init__(self, _graph):
        self.graph = _graph
        self.stack = Queue()
        self.visited_vertices = set()
        self.starting_vertex = list(self.graph.graph.keys())[0]

    def depth_first_search(self):
        self.handle_visited_vertex(self.starting_vertex)
        while not self.stack.is_empty():
            next_vertex = self.stack.peek()
            adjacent_vertex = self.graph.graph.get(next_vertex)[0]
            if adjacent_vertex in self.visited_vertices:
                unvisited_vertex_found = False
                for _adjacent_vertex in self.graph.graph.get(next_vertex):
                    if _adjacent_vertex not in self.visited_vertices:
                        unvisited_vertex_found = True
                        adjacent_vertex = _adjacent_vertex
                        self.handle_visited_vertex(adjacent_vertex)
                        break
                if not unvisited_vertex_found:
                    self.stack.pop()
                    continue
            else:
                self.handle_visited_vertex(adjacent_vertex)
            self.starting_vertex = adjacent_vertex

    def handle_visited_vertex(self, vertex):
        print(vertex, end='\t')
        self.stack.push(vertex)
        self.visited_vertices.add(vertex)

    def dfs(self, vertex=None):
        """
        Depth First search using Recursion
        """
        if not vertex:
            vertex = self.starting_vertex
        self.visited_vertices.add(vertex)
        print(vertex, end='\t')
        for adjacent_vertex in set(self.graph.graph.get(vertex)) - self.visited_vertices:
            if adjacent_vertex not in self.visited_vertices:
                self.dfs(adjacent_vertex)


if __name__ == '__main__':
    graph = Graph()

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

    dfs = DepthFirstSearch(graph)
    dfs.depth_first_search()

    print()
    dfs.visited_vertices = set()
    dfs.starting_vertex = 'S'
    # dfs using recursion
    dfs.dfs()
