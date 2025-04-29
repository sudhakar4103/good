import sys

def prim_mst(graph, n):
    selected = [False] * n
    selected[0] = True  # start from vertex 0
    mst_edges = []
    for _ in range(n - 1):
        min_weight = sys.maxsize
        u = v = -1
        for i in range(n):
            if selected[i]:
                for j, w in enumerate(graph[i]):
                    if not selected[j] and w != 0 and w < min_weight:
                        min_weight = w
                        u, v = i, j
        selected[v] = True
        mst_edges.append((u, v, min_weight))
    return mst_edges

if __name__ == '__main__':
    n = int(input("Number of vertices: "))
    print("Enter adjacency matrix (0 means no edge):")
    graph = [list(map(int, input().split())) for _ in range(n)]
    mst = prim_mst(graph, n)
    print("Edges in MST (u, v, weight):")
    for u, v, w in mst:
        print(u, v, w)
