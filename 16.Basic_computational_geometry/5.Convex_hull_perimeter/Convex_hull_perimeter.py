from math import inf, sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x or ((self.x == other.x) and self.y < other.y)


class Vector:
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def cross_product(self, v):
        result = self.x * v.y - self.y * v.x
        return result

    def length(self):
        result = sqrt(self.x ** 2 + self.y ** 2)
        return result


def slope(point):
    p_0 = points[0]
    if p_0.x != point.x:
        return (p_0.y - point.y) / (p_0.x - point.x)
    return inf


def graham(points):
    convex_hull = []
    points.sort()
    sorted_points = points[:1] + sorted(points[1:], key=slope)
    for point in sorted_points:
        while (
            len(convex_hull) >= 2
            and Vector(convex_hull[-1], convex_hull[-2]).cross_product(
                Vector(convex_hull[-1], point)
            )
            >= 0
        ):
            convex_hull.pop()
        convex_hull.append(point)
    convex_hull.append(convex_hull[0])
    return convex_hull


if __name__ == "__main__":
    n = int(input())
    used = [False] * n
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    convex_hull = graham(points)
    perimeter = 0
    for i in range(len(convex_hull) - 1):
        perimeter += Vector(convex_hull[i], convex_hull[i + 1]).length()
    print(perimeter)
    
    
# 5
# 0 0
# 2 0
# 0 2
# 1 1
# 2 2
#
# 8
