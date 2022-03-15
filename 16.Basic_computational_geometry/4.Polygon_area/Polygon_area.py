class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, point1, point2):
        self.x = point2.x - point1.x
        self.y = point2.y - point1.y

    def cross_product(self, vector):
        result = self.x * vector.y - self.y * vector.x
        return result


if __name__ == "__main__":
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    v = []
    for i in range(n):
        v.append(Vector(points[0], points[i]))
    s = 0
    for i in range(n - 1):
        s += v[i].cross_product(v[(i + 1)])
    print(abs(s) / 2)


# 3
# 1 0
# 0 1
# 1 1
#
# 0.5
