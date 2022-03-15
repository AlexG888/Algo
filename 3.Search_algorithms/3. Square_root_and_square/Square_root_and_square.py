import sys
from math import log


def solve():
    c = float(sys.stdin.readline())
    left = 0
    right = c
    middle = (right + left) / 2
    for i in range(INT):
        if middle * middle + middle ** 0.5 >= c:
            right = middle
        else:
            left = middle
        middle = (left + right) / 2
    print(right)


INT = int(log((10 ** 10 / 10 ** (-6)), 2))

if __name__ == "__main__":
    solve()

# 18.0000000000
#
# 4.0