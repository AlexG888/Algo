import sys


def min_time(n, x, y):
    left = 0
    right = (n - 1) * max(x, y)
    while left < right - 1:
        middle = (left + right) // 2
        if (middle // x + middle // y) < n - 1:
            left = middle
        else:
            right = middle
    return right + min(x, y)


def solve():
    n, x, y = map(int, sys.stdin.readline().split())
    print(min_time(n, x, y))


if __name__ == "__main__":
    solve()


# 5 1 2
#
# 4