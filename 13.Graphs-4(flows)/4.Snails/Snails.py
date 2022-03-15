from math import inf
import sys
import threading
from tkinter.messagebox import YES


def main():
    class Edge:
        def __init__(self, start, end, cap, dist):
            self.start = start
            self.end = end
            self.cap = cap
            self.dist = dist
            self.flow = 0

    class Flow:
        def __init__(self):
            self.adj = [[] for _ in range(n)]

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

        def restore(self, path, start, end):
            path.append(str(start + 1))
            if start == end:
                return
            for edge in self.adj[start]:
                if edge.flow != edge.cap or edge.cap == 0:
                    continue
                else:
                    edge.flow = 0
                    self.adj[edge.end][edge.dist].flow = 0
                    self.restore(path, edge.end, end)
                    break

    n, m, s, t = map(int, input().split())
    g = Flow()
    for _ in range(m):
        u, v = map(int, input().split())
        edge = Edge(u - 1, v - 1, 1, len(g.adj[v - 1]))
        g.adj[u - 1].append(edge)
        r_edge = Edge(v - 1, u - 1, 0, len(g.adj[u - 1]) - 1)
        g.adj[v - 1].append(r_edge)
    s -= 1
    t -= 1
    result = 0
    while True:
        used = [False for _ in range(n)]
        delta = g.push(s, t, inf, used)
        if delta > 0:
            result += delta
        else:
            break
    if result < 2:
        print("NO")
    else:
        result_1 = []
        result_2 = []
        g.restore(result_1, s, t)
        g.restore(result_2, s, t)
        if len(result_1) < len(result_2):
            print("YES")
            print(*result_1)
            print(*result_2)
        else:
            print("YES")
            print(*result_2)
            print(*result_1)


sys.setrecursionlimit(10 ** 9)
threading.stack_size(10 ** 8)
if __name__ == "__main__":
    threading.Thread(target=main).start()

# 3 3 1 3
# 1 2
# 1 3
# 2 3
# 
# YES
# 1 3
# 1 2 3