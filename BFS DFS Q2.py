from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
}

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result

# DFS Function
def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph[node]))

    return result

print("BFS:", bfs(graph, 1))
print("DFS:", dfs(graph, 1))
