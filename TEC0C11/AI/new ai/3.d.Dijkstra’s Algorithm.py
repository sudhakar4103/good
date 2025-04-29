import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in enumerate(graph[u]):
            if w > 0:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
    return dist

if __name__ == '__main__':
    n = int(input("Number of vertices: "))
    print("Enter adjacency matrix (0 means no edge):")
    graph = [list(map(int, input().split())) for _ in range(n)]
    src = int(input("Source vertex: "))
    distances = dijkstra(graph, src)
    print("Shortest distances from vertex", src, "to each vertex:")
    for v, d in enumerate(distances):
        print(f"{src} -> {v} = {d}")
