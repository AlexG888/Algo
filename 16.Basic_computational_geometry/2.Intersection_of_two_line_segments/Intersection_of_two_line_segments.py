class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_in_segment(self, point_a, point_b):
        ab = Vector(point_a, point_b)
        ba = Vector(point_b, point_a)
        ac = Vector(point_a, self)
        bc = Vector(point_b, self)
        cp_ab_ac = ab.cross_product(ac)
        dp_ab_ac = ab.dot_product(ac)
        dp_ba_bc = ba.dot_product(bc)
        if cp_ab_ac == 0 and dp_ab_ac >= 0 and dp_ba_bc >= 0:
            return True


class Vector:
    def __init__(self, point1, point2):
        self.x = point2.x - point1.x
        self.y = point2.y - point1.y

    def cross_product(self, vector):
        result = self.x * vector.y - self.y * vector.x
        return result

    def dot_product(self, vector):
        result = self.x * vector.x + self.y * vector.y
        return result


if __name__ == "__main__":
    a_x, a_y, b_x, b_y = map(int, input().split())
    c_x, c_y, d_x, d_y = map(int, input().split())
    point_a, point_b = Point(a_x, a_y), Point(b_x, b_y)
    point_c, point_d = Point(c_x, c_y), Point(d_x, d_y)
    ab = Vector(point_a, point_b)
    ac = Vector(point_a, point_c)
    ca = Vector(point_c, point_a)
    cb = Vector(point_c, point_b)
    ad = Vector(point_a, point_d)
    cd = Vector(point_c, point_d)
    if (
        point_a.point_in_segment(point_c, point_d)
        or point_b.point_in_segment(point_c, point_d)
        or point_c.point_in_segment(point_a, point_b)
        or point_d.point_in_segment(point_a, point_b)
        or (
            ab.cross_product(ac) * ab.cross_product(ad) < 0
            and cd.cross_product(ca) * cd.cross_product(cb) < 0
        )
    ):
        print("YES")
    else:
        print("NO")


# 5 1 2 6
# 1 1 7 8
#
# YES
