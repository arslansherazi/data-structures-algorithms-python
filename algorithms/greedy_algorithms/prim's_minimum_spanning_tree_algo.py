"""
Complexity ==> O(E log V)
"""
from data_structures.graph.weighted_graph import WeightedGraph


def prims_algo(no_of_vertices: int, _graph: list, _vertices_map: {}):
    selected_vertices = [0] * no_of_vertices
    no_of_selected_edges = 0
    selected_vertices[0] = True
    print("Edge : Weight\n")

    while no_of_selected_edges < no_of_vertices - 1:
        minimum = INF
        x_axis_of_graph = 0
        y_axis_of_graph = 0
        for i in range(no_of_vertices):
            if selected_vertices[i]:
                # find minimum weight edge from the selected vertex
                for j in range(no_of_vertices):
                    if not selected_vertices[j] and _graph[i][j]:
                        if minimum > _graph[i][j]:
                            minimum = _graph[i][j]
                            x_axis_of_graph = i
                            y_axis_of_graph = j
        print(
            _vertices_map.get(x_axis_of_graph) +
            "  -  " +
            _vertices_map.get(y_axis_of_graph) +
            "  :  " +
            str(_graph[x_axis_of_graph][y_axis_of_graph])
        )

        selected_vertices[y_axis_of_graph] = True
        no_of_selected_edges += 1


if __name__ == '__main__':
    INF = 9999999
    graph = WeightedGraph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')

    graph.add_edge(starting_vertex='a', ending_vertex='b', weight=4)
    graph.add_edge(starting_vertex='b', ending_vertex='a', weight=4)
    graph.add_edge(starting_vertex='c', ending_vertex='a', weight=4)
    graph.add_edge(starting_vertex='a', ending_vertex='c', weight=4)
    graph.add_edge(starting_vertex='c', ending_vertex='b', weight=2)
    graph.add_edge(starting_vertex='b', ending_vertex='c', weight=2)
    graph.add_edge(starting_vertex='c', ending_vertex='d', weight=3)
    graph.add_edge(starting_vertex='d', ending_vertex='c', weight=3)
    graph.add_edge(starting_vertex='c', ending_vertex='e', weight=2)
    graph.add_edge(starting_vertex='e', ending_vertex='c', weight=2)
    graph.add_edge(starting_vertex='e', ending_vertex='f', weight=3)
    graph.add_edge(starting_vertex='f', ending_vertex='e', weight=3)
    graph.add_edge(starting_vertex='c', ending_vertex='f', weight=4)
    graph.add_edge(starting_vertex='f', ending_vertex='c', weight=4)
    graph.add_edge(starting_vertex='f', ending_vertex='d', weight=3)
    graph.add_edge(starting_vertex='d', ending_vertex='f', weight=3)

    adjacency_matrix = graph.get_adjacency_matrix()
    vertices_map = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f'
    }

    prims_algo(no_of_vertices=6, _graph=adjacency_matrix, _vertices_map=vertices_map)
