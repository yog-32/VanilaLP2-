from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def dfs_util(graph, v, visited):
    visited.add(v)
    print(v, end=' ')

    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs_util(graph, neighbor, visited)

def dfs(graph, v):
    visited = set()
    dfs_util(graph, v, visited)

def bfs(graph, v):
    visited = set()
    queue = [v]
    visited.add(v)

    while queue:
        v = queue.pop(0)
        print(v, end=' ')

        for neighbor in graph[v]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example usage:
graph = defaultdict(list)
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 3, 3)

print("DFS traversal starting from vertex 2:")
dfs(graph, 2)
print("\nBFS traversal starting from vertex 2:")
bfs(graph, 2)
