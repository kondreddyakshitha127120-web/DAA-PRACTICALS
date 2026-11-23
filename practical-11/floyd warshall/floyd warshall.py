def floyd_warshall(graph):
    """
    Computes all-pairs shortest paths using the Floyd-Warshall algorithm.
    :param graph: 2D list (matrix) where graph[i][j] is the weight of edge i -> j
    :return: 2D list of shortest distances between all pairs
    """
    num_vertices = len(graph)
    
    # Create a deep copy of the graph matrix to store distances
    dist = [list(row) for row in graph]

    # Core Algorithm: Try every vertex 'k' as an intermediate node
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance if passing through 'k' offers a shorter path
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# --- Example Usage ---
if __name__ == "__main__":
    INF = float('inf')
    
    # 4-vertex graph example matrix
    # Node connections:
    # 0 -> 1 (weight 3), 0 -> 3 (weight 7)
    # 1 -> 0 (weight 8), 1 -> 2 (weight 2)
    # 2 -> 0 (weight 5), 2 -> 3 (weight 1)
    # 3 -> 0 (weight 2)
    graph_matrix = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]

    shortest_paths = floyd_warshall(graph_matrix)

    print("Shortest distance matrix between all pairs:")
    for row in shortest_paths:
        print([f"INF" if x == INF else x for x in row])
