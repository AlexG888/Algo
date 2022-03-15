import sys


class DSU:
    def __init__(self, min_element, max_element, cnt):
        self.min = min_element
        self.max = max_element
        self.cnt = cnt

    def get_DSU(self):
        return " ".join([str(self.min + 1), str(self.max + 1), str(self.cnt)])


def join(x, y):
    x = get(x)
    y = get(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        x, y = y, x
    if rank[x] == rank[y]:
        rank[y] += 1
    prev[x] = y
    dsu[y].min = min(dsu[y].min, dsu[x].min)
    dsu[y].max = max(dsu[y].max, dsu[x].max)
    dsu[y].cnt += dsu[x].cnt


def get(x):
    if prev[x] != x:
        prev[x] = get(prev[x])
    return prev[x]


def load_DSU():
    n = int(input())
    rank = [0 for _ in range(n)]
    prev = [i for i in range(n)]
    dsu = [DSU(i, i, 1) for i in range(n)]
    return rank, prev, dsu


if __name__ == "__main__":
    rank, prev, dsu = load_DSU()
    for line in sys.stdin:
        l = list(line.split())
        if l[0] == "union":
            join(int(l[1]) - 1, int(l[2]) - 1)
        elif l[0] == "get":
            point = get(int(l[1]) - 1)
            print(dsu[point].get_DSU())

# 5
# union 1 2
# get 3
# get 2
# union 2 3
# get 2
# union 1 3
# get 5
# union 4 5
# get 5
# union 4 1
# get 5
#
# 3 3 1
# 1 2 2
# 1 3 3
# 5 5 1
# 4 5 2
# 1 5 5
