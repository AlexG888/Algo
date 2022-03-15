from math import inf
from collections import deque, defaultdict


class Edge:
    def __init__(self, start, end, flow, cap, r_edge):
        self.start = start
        self.end = end
        self.flow = flow
        self.cap = cap
        self.r_edge = r_edge


def EdmondsKarp():
    n = int(input())
    m = int(input())
    s, t = 0, n - 1
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge = Edge(a - 1, b - 1, 0, c, None)
        r_edge = Edge(b - 1, a - 1, 0, c, edge)
        edge.r_edge = r_edge
        edges.append(edge)
        edges.append(r_edge)
    out_edges = defaultdict(list)
    for e_idx, e in enumerate(edges):
        out_edges[e.start].append(e_idx)
    while True:
        queue = deque()
        queue.append(s)
        r_edges = [None] * n
        r_edges[s] = 0
        while queue:
            v = queue.popleft()
            if v == t:
                break
            for e_idx in out_edges[v]:
                next_edge = edges[e_idx]
                if r_edges[next_edge.end] is None and next_edge.flow < next_edge.cap:
                    r_edges[next_edge.end] = e_idx
                    queue.append(next_edge.end)
        if r_edges[t] is None:
            break
        min_flow_cap = inf
        tmp_v_idx = t
        while tmp_v_idx != s:
            edge = edges[r_edges[tmp_v_idx]]
            free_capacity = edge.cap - edge.flow
            if free_capacity < min_flow_cap:
                min_flow_cap = free_capacity
            tmp_v_idx = edge.start
        tmp_v_idx = t
        while tmp_v_idx != s:
            edge = edges[r_edges[tmp_v_idx]]
            edge.flow += min_flow_cap
            edge.r_edge.flow -= min_flow_cap
            tmp_v_idx = edge.start
    max_flow = 0
    for e_idx in out_edges[s]:
        max_flow += edges[e_idx].flow
    print(max_flow)
    for e_idx in range(m):
        edge = edges[e_idx * 2]
        print(edge.flow)


if __name__ == "__main__":
    EdmondsKarp()


# 2 2
# A#
# #B
# 
# 0
# A#
# #B