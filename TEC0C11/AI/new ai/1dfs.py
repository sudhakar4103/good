from collections import deque

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

if __name__ == '__main__':
    n = int(input('Number of vertices: '))
    m = int(input('Number of edges: '))
    graph = {i: [] for i in range(n)}
    print('Enter edges (u v):')
    for _ in range(m):
        u, v = map(int, input().split())  # zero-based
        graph[u].append(v)
        graph[v].append(u)

    start = int(input('Start node: '))
    print('\nDFS order:', end=' ')
    dfs(graph, start)
    print('\nBFS order:', end=' ')
    bfs(graph, start)