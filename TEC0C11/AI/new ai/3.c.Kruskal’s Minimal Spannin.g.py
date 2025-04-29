class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def kruskal_mst(edges, n):
    uf = UnionFind(n)
    mst = []
    edges.sort(key=lambda x: x[2])  # sort by weight
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            if len(mst) == n - 1:
                break
    return mst

if __name__ == '__main__':
    n = int(input("Number of vertices: "))
    m = int(input("Number of edges: "))
    print("Enter edges (u v weight):")
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    mst = kruskal_mst(edges, n)
    print("Edges in MST (u, v, weight):")
    for u, v, w in mst:
        print(u, v, w)
