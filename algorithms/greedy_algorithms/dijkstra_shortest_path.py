from queue import PriorityQueue

from data_structures.graph.weighted_graph import WeightedGraph


class DijkstraShortestPath:
    def __init__(self, _graph):
        self.graph = _graph

    def dijkstra(self, source_vertex, dest_vertex):
        """
        Dijkstra algorithm

        :param source_vertex: source vertex
        :param dest_vertex: destination vertex

        :return: vertices parent map from source vertex
        """
        visited_vertices = set()
        visiting_vertices_cost_map = {source_vertex: 0}
        vertices_parent_map = {source_vertex: None}
        priority_queue = PriorityQueue()  # min priority queue

        priority_queue.put((0, source_vertex))
        while priority_queue:
            while not priority_queue.empty():
                _, vertex = priority_queue.get()
                if vertex not in visited_vertices:
                    break
            else:
                break
            visited_vertices.add(vertex)
            if vertex == dest_vertex:
                break
            for vertex_data in self.graph[vertex]:
                neighbor = vertex_data[0]
                distance = vertex_data[1]
                if neighbor in visited_vertices:
                    continue
                old_cost = visiting_vertices_cost_map.get(neighbor, float('inf'))
                new_cost = visiting_vertices_cost_map[vertex] + distance
                if new_cost < old_cost:
                    priority_queue.put((new_cost, neighbor))
                    visiting_vertices_cost_map[neighbor] = new_cost
                    vertices_parent_map[neighbor] = vertex

        return vertices_parent_map

    @staticmethod
    def display_shortest_path(vertices_parent_map, dest_vertex):
        """
        displays shortest path using vertices parent map generated through dijkstra algorithm

        :param vertices_parent_map: vertices parent map
        :param dest_vertex: destination vertex

        :return: shortest path
        """
        if dest_vertex not in vertices_parent_map:
            return None

        _vertex = dest_vertex

        shortest_path = []
        while _vertex:
            shortest_path.append(_vertex)
            _vertex = vertices_parent_map[_vertex]

        for _vertex in shortest_path[::-1]:
            print(_vertex, end="  -> ")


if __name__ == '__main__':
    graph = WeightedGraph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')

    graph.add_edge(starting_vertex='a', ending_vertex='b', weight=4)
    graph.add_edge(starting_vertex='a', ending_vertex='c', weight=4)
    graph.add_edge(starting_vertex='b', ending_vertex='c', weight=2)
    graph.add_edge(starting_vertex='c', ending_vertex='d', weight=3)
    graph.add_edge(starting_vertex='c', ending_vertex='e', weight=1)
    graph.add_edge(starting_vertex='c', ending_vertex='f', weight=6)
    graph.add_edge(starting_vertex='e', ending_vertex='f', weight=3)
    graph.add_edge(starting_vertex='d', ending_vertex='f', weight=2)

    dijkstra_shortest_path = DijkstraShortestPath(_graph=graph.weighted_graph)
    distance_map = dijkstra_shortest_path.dijkstra(source_vertex='a', dest_vertex='f')
    dijkstra_shortest_path.display_shortest_path(vertices_parent_map=distance_map, dest_vertex='f')
