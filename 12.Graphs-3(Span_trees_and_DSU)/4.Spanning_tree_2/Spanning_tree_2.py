class Graph:
    def __init__(self, n, m):
        self.rank = [0 for _ in range(n)]
        self.edges = [None for _ in range(m)]
        self.parent = [i for i in range(n)]

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x, y = self.get(x), self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y


class Edge:
    def __init__(self, prev, nxt, weight):
        self.prev = prev
        self.nxt = nxt
        self.weight = weight


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n, m)
    for i in range(m):
        b, e, w = map(int, input().split())
        g.edges[i] = Edge(b - 1, e - 1, w)
    g.edges.sort(key=lambda e: e.weight)
    result = 0
    for edge in g.edges:
        if g.get(edge.prev) != g.get(edge.nxt):
            result += edge.weight
            g.join(edge.prev, edge.nxt)
    print(result)

# 4 4
# 1 2 1
# 2 3 2
# 3 4 5
# 4 1 4
# 
# 7