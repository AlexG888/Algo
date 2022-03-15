import math
 
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def point_in_segment(self, a, b):
        if min(a.x, b.x) <= self.x <= max(a.x, b.x) and \
            min(a.y, b.y) <= self.y <= max(a.y, b.y):
            return True
 
 
class Vector:
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y
 
    def dot_product(self, vector):
        result = self.x * vector.x + self.y * vector.y
        return result
 
    def cross_product(self, vector):
        result = self.x * vector.y - self.y * vector.x
        return result
 
    def angle(self, vector):
        result = math.atan2(self.cross_product(vector), self.dot_product(vector))
        return result
 
 
EPS = 10 ** (-9)
 
if __name__ == "__main__":
    n, point_x, point_y = map(int, input().split())
    point = Point(point_x, point_y)
    vertex_array = []
    ang = 0
    on_edge = False
    for i in range(n):
        x, y = map(int, input().split())
        vertex_array.append(Point(x, y))
    vertex_array.append(vertex_array[0])
    for i in range(n):
        pv_1 = Vector(point, vertex_array[i])
        pv_2 = Vector(point, vertex_array[i + 1])
        if pv_1.cross_product(pv_2) == 0 and point.point_in_segment(
            vertex_array[i], vertex_array[i + 1]
        ):
            on_edge = True
            break
        ang += pv_1.angle(pv_2)
    if on_edge or abs(ang) >= EPS:
        print("YES")
    else:
        print("NO")
        

# 3 2 3
# 1 1
# 10 2
# 2 8
#
# YES