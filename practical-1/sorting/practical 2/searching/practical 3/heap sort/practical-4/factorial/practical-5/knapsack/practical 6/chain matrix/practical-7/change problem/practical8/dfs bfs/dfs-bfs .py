
from collections import deque

# Create graph
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# BFS Function
def BFS(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# DFS Function
def DFS(start):
    visited = set()

    def dfs(node):
        visited.add(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

    print("DFS Traversal:", end=" ")
    dfs(start)

# Starting vertex
start = input("\nEnter starting vertex: ")

BFS(start)
print()
DFS(start)
