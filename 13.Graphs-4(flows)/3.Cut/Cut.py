from math import inf


class Edge:
    def __init__(self, start, end, cap, dist):
        self.start = start
        self.end = end
        self.cap = cap
        self.dist = dist
        self.flow = 0


class Flow:
    def __init__(self, n):
        self.size = n
        self.adj = [[] for _ in range(self.size)]
        self.edge_order = []
        self.cut_edges = []
        self.total_caps = 0

    def push(self, v, t, cur_flow, used):
        used[v] = True
        if v == t:
            return cur_flow
        for edge in self.adj[v]:
            u = edge.end
            if not used[u] and edge.flow < edge.cap:
                next_flow = min(cur_flow, edge.cap - edge.flow)
                delta = self.push(u, t, next_flow, used)
                if delta > 0:
                    edge.flow += delta
                    back_edge = self.adj[u][edge.dist]
                    back_edge.flow -= delta
                    return delta
        return False

    def bfs(self):
        d = [-1 for _ in range(self.size)]
        d[s] = 0
        queue = [s]
        while queue:
            v = queue.pop(0)
            for edge in self.adj[v]:
                u = edge.end
                if edge.flow < edge.cap and d[u] == -1:
                    d[u] = d[v] + 1
                    queue.append(u)
        return d[t] != -1

    def change(self, in_s, v):
        if in_s[v]:
            return
        in_s[v] = True
        for edge in self.adj[v]:
            if edge.flow != edge.cap:
                self.change(in_s, edge.end)

    def restore(self):
        in_s = [False for _ in range(self.size)]
        self.change(in_s, s)
        i = 0
        for edge in self.edge_order:
            u = edge.start
            v = edge.end
            i += 1
            if in_s[u] == in_s[v]:
                continue
            self.cut_edges.append(str(i))
            self.total_caps += edge.cap


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Flow(n)
    for i in range(m):
        u, v, w = map(int, input().split())
        edge = Edge(u - 1, v - 1, w, len(g.adj[v - 1]))
        g.adj[u - 1].append(edge)
        r_edge = Edge(v - 1, u - 1, w, len(g.adj[u - 1]) - 1)
        g.adj[v - 1].append(r_edge)
        g.edge_order.append(g.adj[u - 1][-1])
    s, t = 0, g.size - 1
    result = 0
    while g.bfs():
        used = [False for _ in range(g.size)]
        delta = g.push(s, t, inf, used)
        if delta > 0:
            result += delta
        else:
            break
    g.restore()
    print(len(g.cut_edges), g.total_caps)
    print(*g.cut_edges)

# 3 3
# 1 2 3
# 1 3 5
# 3 2 7
# 
# 2 8
# 1 2