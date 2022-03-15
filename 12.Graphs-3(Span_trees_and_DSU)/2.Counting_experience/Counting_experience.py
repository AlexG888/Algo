import sys


class Counting_experience:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.prev = [i for i in range(n)]
        self.next = [[] for _ in range(n)]
        self.expirience = [0 for _ in range(n)]

    def get(self, x):
        if self.prev[x] != x:
            self.prev[x] = self.get(self.prev[x])
        return self.prev[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.prev[x] = y
        self.next[y].append(x)
        self.next[y] += self.next[x]

    def update_expirience(self, x, v):
        point = self.get(x)
        self.expirience[point] += v
        for i in self.next[point]:
            self.expirience[i] += v


if __name__ == "__main__":
    n, m = map(int, sys.stdin.buffer.readline().decode().split())
    c = Counting_experience(n)
    for i in range(m):
        l = list(sys.stdin.buffer.readline().decode().split())
        if l[0] == "join":
            c.join(int(l[1]) - 1, int(l[2]) - 1)
        elif l[0] == "get":
            print(str(c.expirience[int(l[1]) - 1]))
        elif l[0] == "add":
            c.update_expirience(int(l[1]) - 1, int(l[2]))

# 3 6
# add 1 100
# join 1 3
# add 1 50
# get 1
# get 2
# get 3
# 
# 150
# 0
# 50