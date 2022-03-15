from math import inf


class Edge:
    def __init__(self, start, end, cap, dist):
        self.start = start
        self.end = end
        self.dist = dist
        self.cap = cap
        self.flow = 0


class Flow:
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]

    def push_flow(self, v, t, cur_flow, used):
        used[v] = True
        if v == t:
            return cur_flow
        for edge in self.adj[v]:
            u = edge.end
            if not used[u] and edge.flow < edge.cap:
                next_flow = min(cur_flow, edge.cap - edge.flow)
                delta = self.push_flow(u, t, next_flow, used)
                if delta > 0:
                    edge.flow += delta
                    back_edge = self.adj[u][edge.dist]
                    back_edge.flow -= delta
                    return delta
        return False


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    s, t = 0, n - 1
    g = Flow(n)
    for i in range(m):
        a, b, c = map(int, input().split())
        edge = Edge(a - 1, b - 1, c, len(g.adj[b - 1]))
        g.adj[a - 1].append(edge)
        r_edge = Edge(b - 1, a - 1, c, len(g.adj[a - 1]) - 1)
        g.adj[b - 1].append(r_edge)
    result = 0
    while True:
        used = [False for i in range(n)]
        delta = g.push_flow(s, t, inf, used)
        if delta > 0:
            result += delta
        else:
            break
    print(result)

# 2
# 2
# 1 2 1
# 2 1 3
# 
# 4