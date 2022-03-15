class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, point1, point2):
        self.x = point2.x - point1.x
        self.y = point2.y - point1.y

    def cross_product(self, v):
        return self.x * v.y - self.y * v.x

    def dot_product(self, v):
        return self.x * v.x + self.y * v.y


if __name__ == "__main__":
    c_x, c_y, a_x, a_y, b_x, b_y = map(int, input().split())
    point_a, point_b, point_c = Point(a_x, a_y), Point(b_x, b_y), Point(c_x, c_y)
    ab = Vector(point_a, point_b)
    ba = Vector(point_b, point_a)
    ac = Vector(point_a, point_c)
    bc = Vector(point_b, point_c)
    cp_ab_ac = ab.cross_product(ac)
    dp_ab_ac = ab.dot_product(ac)
    dp_ba_bc = ba.dot_product(bc)
    print("YES" if cp_ab_ac == 0 and dp_ab_ac >= 0 and dp_ba_bc >= 0 else "NO")


# 3 3 1 2 5 4
#
# YES

# 4 2 4 2 4 5
#
# YES
