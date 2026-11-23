def kruskal(vertices, edges):
    # Map each vertex to its own unique set ID initially
    parent = {v: v for v in vertices}
    
    # Helper to find the ultimate root ID of a vertex
    find = lambda x: x if parent[x] == x else find(parent[x])

    mst = []
    # Loop through edges sorted by their weight (the first element of the tuple)
    for weight, u, v in sorted(edges):
        root_u, root_v = find(u), find(v)
        
        # If roots are different, adding this edge won't create a cycle
        if root_u != root_v:
            parent[root_u] = root_v  # Combine the sets
            mst.append((u, v, weight))
            
    return mst

# --- Example ---
nodes = ['A', 'B', 'C', 'D']
# Format: (weight, node1, node2)
graph_edges = [(1, 'A', 'B'), (4, 'B', 'C'), (2, 'A', 'C'), (3, 'C', 'D')]

print("Minimum Spanning Tree:", kruskal(nodes, graph_edges))
