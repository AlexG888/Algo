from sys import setrecursionlimit
import threading
from collections import defaultdict
 
 
class Graph:
    def __init__(self, size):
        self.graph = defaultdict(list)
        self.used = [0] * (size + 1)
 
    def add(self, u, v):
        self.graph[u].append(v)
 
    def dfs(self, start, vert):
        self.used[start] = vert
        for u in self.graph[start]:
            if self.used[u] == 0:
                self.dfs(u, vert)
 
 
def main():
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        b, e = map(int, input().split())
        g.add(b, e)
        g.add(e, b)
 
    for i in range(1, n + 1):
        if i not in g.graph.keys():
            g.add(i, i)
 
    cnt = 0
    for v in range(1, n + 1):
        if g.used[v] == 0:
            cnt += 1
            g.dfs(v, cnt)
 
    print(cnt)
    print(*g.used[1:])
 
 
setrecursionlimit(10 ** 9)
threading.stack_size(10 ** 8)
thread = threading.Thread(target=main)
thread.start()



# 3 1
# 1 2
# 
# 2
# 1 1 2

# 4 2
# 1 3
# 2 4
# 
# 2
# 1 2 1 2