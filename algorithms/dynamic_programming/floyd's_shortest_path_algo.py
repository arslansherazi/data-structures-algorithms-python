from data_structures.graph.weighted_graph import WeightedGraph


class FloydWarshall:
    def __init__(
            self, no_of_vertices: int, _graph_adjacency_matrix: list, _distance_table: list, _sequence_table: list
    ):
        self.no_of_vertices = no_of_vertices
        self.graph_adjacency_matrix = _graph_adjacency_matrix
        self.distance_table = _distance_table
        self.sequence_table = _sequence_table

    def initialize(self):
        for i in range(self.no_of_vertices):
            for j in range(self.no_of_vertices):
                self.distance_table[i][j] = self.graph_adjacency_matrix[i][j]

                # No edge between vertex i and j
                if self.graph_adjacency_matrix[i][j] == INF:
                    self.sequence_table[i][j] = -1
                else:
                    self.sequence_table[i][j] = j

    def floyd_warshall_algo(self):
        for k in range(self.no_of_vertices):
            for i in range(self.no_of_vertices):
                for j in range(self.no_of_vertices):

                    # We cannot travel through edge that doesn't exist
                    if self.distance_table[i][k] == float('INF') or self.distance_table[k][j] == float('INF'):
                        continue

                    if self.distance_table[i][j] > self.distance_table[i][k] + self.distance_table[k][j]:
                        self.distance_table[i][j] = self.distance_table[i][k] + self.distance_table[k][j]
                        self.sequence_table[i][j] = self.sequence_table[i][k]

    def get_shortest_path(self, _source_vertex, _destination_vertex):
        # If there's no path between source vertex and destination vertex, simply return an empty array
        if self.sequence_table[_source_vertex][_destination_vertex] == -1:
            return {}

        # Storing the path in a vector
        _path = [_source_vertex]
        while _source_vertex != _destination_vertex:
            _source_vertex = self.sequence_table[_source_vertex][_destination_vertex]
            _path.append(_source_vertex)

        return _path

    @staticmethod
    def generate_vertices_map(_graph_vertices_integer_map: dict):
        """
        Map integer vertices with actual vertices names
        """
        _vertices_map = {}
        for vertex, vertex_integer in _graph_vertices_integer_map.items():
            _vertices_map[vertex_integer] = vertex
        return _vertices_map

    @staticmethod
    def print_path(_path: dict, _vertices_map: dict):
        n = len(_path)
        for i in range(n - 1):
            print(_vertices_map.get(_path[i]), end=" -> ")
        print(_vertices_map.get(_path[n - 1]))


if __name__ == '__main__':
    graph = WeightedGraph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')

    graph.add_edge(starting_vertex='a', ending_vertex='b', weight=5)
    graph.add_edge(starting_vertex='a', ending_vertex='c', weight=1)
    graph.add_edge(starting_vertex='b', ending_vertex='c', weight=3)
    graph.add_edge(starting_vertex='c', ending_vertex='a', weight=1)
    graph.add_edge(starting_vertex='c', ending_vertex='d', weight=4)
    graph.add_edge(starting_vertex='d', ending_vertex='a', weight=2)

    graph_adjacency_matrix = graph.get_adjacency_matrix()

    MAXM = 100
    INF = float('INF')

    distance_table = [[-1 for _ in range(MAXM)] for _ in range(MAXM)]
    sequence_table = [[-1 for _ in range(MAXM)] for _ in range(MAXM)]

    floyd_warshall = FloydWarshall(
        no_of_vertices=len(graph.weighted_graph.keys()), _graph_adjacency_matrix=graph_adjacency_matrix, _distance_table=distance_table,
        _sequence_table=sequence_table
    )

    floyd_warshall.initialize()

    floyd_warshall.floyd_warshall_algo()

    graph_vertices_integer_map = graph.get_vertices_integer_map()
    source_vertex = graph_vertices_integer_map.get('a')
    destination_vertex = graph_vertices_integer_map.get('d')

    path = floyd_warshall.get_shortest_path(_source_vertex=source_vertex, _destination_vertex=destination_vertex)
    vertices_map = floyd_warshall.generate_vertices_map(graph_vertices_integer_map)

    floyd_warshall.print_path(path, vertices_map)


