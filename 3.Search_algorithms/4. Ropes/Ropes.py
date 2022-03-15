import sys


def counting_ropes(k, sum_lens, len_ropes):
    if sum_lens < k:
        return 0
    left = 0
    right = sum_lens // k + 1
    while left < right - 1:
        middle = (right + left) // 2
        summ = 0
        for i in len_ropes:
            summ += i // middle
        if summ < k:
            right = middle
        else:
            left = middle
    return left


def solve():
    n, k = map(int, sys.stdin.readline().split())
    len_ropes = []
    sum_lens = 0
    for _ in range(n):
        i = int(sys.stdin.readline())
        len_ropes.append(i)
        sum_lens += i
    print(counting_ropes(k, sum_lens, len_ropes))


if __name__ == "__main__":
    solve()

# 4 11
# 802
# 743
# 457
# 539
#
# 200