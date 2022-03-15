import sys
from math import log, sqrt


def t(Oy, m, Vp, Vf):
    return sqrt((1 - Oy) ** 2 + m ** 2) / Vp + sqrt(Oy ** 2 + (1 - m) ** 2) / Vf


def search_Ox(Vp, Vf, Oy):
    left = 0
    right = 1

    for i in range(INT):
        if right - left > EPS:
            middle1 = left + (right - left) / 3
            middle2 = right - (right - left) / 3
            t1 = t(Oy, middle1, Vp, Vf)
            t2 = t(Oy, middle2, Vp, Vf)
            if t1 > t2:
                left = middle1
            else:
                right = middle2
    return right


def solve():
    Vp, Vf = map(int, sys.stdin.readline().split())
    Oy = float(sys.stdin.readline())
    print(search_Ox(Vp, Vf, Oy))


INT = int(log((10 ** 5 / 10 ** (-4)), 1.5))
EPS = 10 ** (-4)

if __name__ == "__main__":
    solve()

# 5 3
# 0.4
#
# 0.7833348751747266