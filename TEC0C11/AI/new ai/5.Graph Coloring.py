def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    def is_valid(node, c):
        for nei in graph[node]:
            if color[nei] == c:
                return False
        return True

    def backtrack(node=0):
        if node == n:
            return True
        for c in range(1, m + 1):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
        color[node] = 0
        return False

    if backtrack():
        return color
    return None

if __name__ == '__main__':
    n = int(input('Number of vertices: '))
    e = int(input('Number of edges: '))
    graph = {i: [] for i in range(n)}
    print('Enter edges (u v):')
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    m = int(input('Number of colors: '))
    sol = graph_coloring(graph, m)
    if sol:
        print('Coloring:', sol)
    else:
        print('No valid coloring')
