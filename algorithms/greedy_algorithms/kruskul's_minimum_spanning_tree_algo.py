class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, source_vertex, dest_vertex, weight):
        self.graph.append([source_vertex, dest_vertex, weight])

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def apply_union(self, parent, rank, source_vertex, dest_vertex):
        """
        Checks the circuit in the Minimum Spanning Tree
        """
        x_root = self.find(parent, source_vertex)
        y_root = self.find(parent, dest_vertex)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_algo(self):
        result = []
        i, edge = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while edge < self.vertices - 1:
            source_vertex, dest_vertex, weight = self.graph[i]
            i = i + 1
            x_vertex = self.find(parent, source_vertex)
            y_vertex = self.find(parent, dest_vertex)
            if x_vertex != y_vertex:
                edge = edge + 1
                result.append([source_vertex, dest_vertex, weight])
                self.apply_union(parent, rank, x_vertex, y_vertex)

        total_weight = 0
        for source_vertex, dest_vertex, weight in result:
            total_weight += weight
            print(f'{source_vertex}  ->  {dest_vertex}  :  {weight}')
        print(f'Total Weight: {total_weight}')


if __name__ == '__main__':
    g = Graph(vertices=4)

    g.add_edge(source_vertex=0, dest_vertex=1, weight=2)
    g.add_edge(source_vertex=0, dest_vertex=3, weight=5)
    g.add_edge(source_vertex=0, dest_vertex=2, weight=1)
    g.add_edge(source_vertex=2, dest_vertex=3, weight=3)
    g.add_edge(source_vertex=1, dest_vertex=2, weight=12)
    g.add_edge(source_vertex=2, dest_vertex=1, weight=2)

    g.kruskal_algo()
