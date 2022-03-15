import sys


def solve(n, x, y, a0, m, z, t, b0, div_a, div_b):
    if m == 0:
        return 0
    else:
        a = post_sum = [0] * n
        b = [0] * 2 * m
        c = [0] * 2 * m
        a[0] = a0
        b[0] = b0
        c[0] = b0 % n
        for i in range(1, n):
            a[i] = (x * a[i - 1] + y) % div_a
        for i in range(1, len(b)):
            b[i] = (z * b[i - 1] + t) % div_b
            c[i] = b[i] % n
        post_sum[0] = a[0]
        for i in range(1, n):
            post_sum[i] = post_sum[i - 1] + a[i]
        result = 0
        for i in range(m):
            left = min(c[2 * i], c[2 * i + 1])
            right = max(c[2 * i], c[2 * i + 1])
            if left == 0:
                result += post_sum[right]
            else:
                result += post_sum[right] - post_sum[left - 1]
        return result


DIVISOR_A = 2 ** 16
DIVISOR_B = 2 ** 30
    
if __name__ == "__main__":
    n, x, y, a0 = list(map(int, sys.stdin.readline().split()))
    m, z, t, b0 = list(map(int, sys.stdin.readline().split()))
    print(solve(n, x, y, a0, m, z, t, b0, DIVISOR_A, DIVISOR_B))


# 3 1 2 3
# 3 1 -1 4
#
# 23
