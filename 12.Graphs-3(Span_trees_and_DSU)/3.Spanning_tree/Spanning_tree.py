from math import inf, sqrt


class Prim:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.dist = [inf] * num_vertices
        self.points = []
        self.used = set()

    def add_point(self, begin, end):
        self.points.append([begin, end])

    def prim(self):
        result = 0
        self.dist[0] = 0
        for i in range(self.num_vertices):
            min_dist = inf
            for j in range(self.num_vertices):
                if j not in self.used and self.dist[j] < min_dist:
                    min_dist = self.dist[j]
                    u = j
            result += min_dist
            self.used.add(u)
            for j in range(self.num_vertices):
                self.dist[j] = min(self.dist[j], self.distance(u, j))
        return result

    def distance(self, begin, end):
        x0, y0 = self.points[begin]
        x1, y1 = self.points[end]
        return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)


if __name__ == "__main__":
    num_vertices = int(input())
    p = Prim(num_vertices)
    for _ in range(num_vertices):
        begin, end = [int(x) for x in input().split()]
        p.add_point(begin, end)
    print(p.prim())


# 2
# 0 0
# 1 1
#
# 1.4142135624
