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

                # No edge between node i and j
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

    def get_shortest_path(self, source_vertex, destination_vertex):
        # If there's no path between source vertex and destination vertex, simply return an empty array
        if self.sequence_table[source_vertex][destination_vertex] == -1:
            return {}

        # Storing the path in a vector
        _path = [source_vertex]
        while source_vertex != destination_vertex:
            source_vertex = self.sequence_table[source_vertex][destination_vertex]
            _path.append(source_vertex)

        return _path

    @staticmethod
    def print_path(path: dict):
        n = len(path)
        for i in range(n - 1):
            print(path[i], end=" -> ")
        print(path[n - 1])


if __name__ == '__main__':
    MAXM = 100
    INF = float('INF')

    distance_table = [[-1 for _ in range(MAXM)] for _ in range(MAXM)]
    sequence_table = [[-1 for _ in range(MAXM)] for _ in range(MAXM)]

    graph_adjacency_matrix = [
        [0, 5, 1, 2],    # vertex-0
        [5, 0, 3, INF],  # vertex-1
        [1, 3, 0, 4],    # vertex-2
        [2, INF, 4, 0]   # vertex-3
    ]

    floyd_warshall = FloydWarshall(
        no_of_vertices=4, _graph_adjacency_matrix=graph_adjacency_matrix, _distance_table=distance_table,
        _sequence_table=sequence_table
    )

    floyd_warshall.initialize()

    floyd_warshall.floyd_warshall_algo()

    path = floyd_warshall.get_shortest_path(source_vertex=1, destination_vertex=3)

    floyd_warshall.print_path(path)


