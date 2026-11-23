
# Prim's Algorithm

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[0] * n for _ in range(n)]

print("Enter edges (u v weight):")
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

visited = [False] * n
visited[0] = True

total_cost = 0
print("\nMinimum Spanning Tree:")

for _ in range(n - 1):
    minimum = float('inf')
    x = -1
    y = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    if x == -1:
        print("Graph is not connected!")
        break

    print(x, "--", y, ":", minimum)
    total_cost += minimum
    visited[y] = True

else:
    print("Total Minimum Cost:", total_cost)
