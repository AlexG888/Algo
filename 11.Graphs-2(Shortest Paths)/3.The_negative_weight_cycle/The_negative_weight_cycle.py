from itertools import product
from math import inf


class Graph:
    def __init__(self):
        self.start = -1
        self.adj_matrix = []
        self.nxt = [[v for v in range(n)] for _ in range(n)]

    def update_dist(self):
        for i, j in product(range(n), repeat=2):
            if self.adj_matrix[i][j] == CONST_NUM:
                self.adj_matrix[i][j] = inf

    def floyd(self):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (
                        self.adj_matrix[i][k] + self.adj_matrix[k][j]
                        < self.adj_matrix[i][j]
                    ):
                        self.adj_matrix[i][j] = (
                            self.adj_matrix[i][k] + self.adj_matrix[k][j]
                        )
                        self.nxt[i][j] = self.nxt[i][k]
            for u in range(n):
                if self.adj_matrix[u][u] < 0:
                    self.start = u
                    break
            if self.start >= 0:
                break


def main():
    g = Graph()
    g.adj_matrix = [list(map(int, input().split())) for _ in range(n)]
    g.update_dist()
    g.floyd()
    if not g.start >= 0:
        print("NO")
    else:
        u = g.start
        result = []
        result_set = set()
        while u not in result_set:
            result.append(u + 1)
            result_set.add(u)
            u = g.nxt[u][g.start]
        print("YES", len(result), sep="\n")
        for element in result:
            print(element, end=" ")


CONST_NUM = 100000

if __name__ == "__main__":
    n = int(input())
    main()


# 2
# 0 -1
# -1 0
#
# YES
# 2
# 2 1