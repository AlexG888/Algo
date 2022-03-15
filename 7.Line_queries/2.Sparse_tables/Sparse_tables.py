def solve(n, m, a1, u1, v1):
    a = [0] * n
    a[0] = a1
    for i in range(1, n):
        a[i] = (CONST1_FOR_A * a[i - 1] + CONST2_FOR_A) % CONST3_FOR_A
    log2arr = [0] * (n + 1)
    for i in range(2, n + 1):
        log2arr[i] = log2arr[i - 1]
        if (1 << log2arr[i]) * 2 <= i:
            log2arr[i] += 1
    power2arr = [2 ** i for i in range(log2arr[-1] + 1)]
    sparse = [[None] * (log2arr[n - i] + 1) for i in range(n)]
    for i in range(n):
        sparse[i][0] = a[i]
    for i in range(1, len(sparse[0])):
        for j in range(n - power2arr[i] + 1):
            sparse[j][i] = min(sparse[j][i - 1], sparse[j + power2arr[i - 1]][i - 1])
    u_next, v_next = u1, v1
    for i in range(1, m + 1):
        u, v = u_next, v_next
        if v >= u:
            k = log2arr[v - u]
            r = min(sparse[u - 1][k], sparse[v - power2arr[k]][k])
        else:
            k = log2arr[u - v]
            r = min(sparse[v - 1][k], sparse[u - power2arr[k]][k])
        u_next = ((CONST1_FOR_U * u + CONST2_FOR_U + r + CONST3_FOR_U * i) % n) + 1
        v_next = ((CONST1_FOR_V * v + CONST2_FOR_V + r + CONST3_FOR_V * i) % n) + 1
    return print(u, v, r)


CONST1_FOR_A = 23
CONST2_FOR_A = 21563
CONST3_FOR_A = 16714589
CONST1_FOR_U = 17
CONST2_FOR_U = 751
CONST3_FOR_U = 2
CONST1_FOR_V = 13
CONST2_FOR_V = 593
CONST3_FOR_V = 5


if __name__ == "__main__":
    n, m, a1 = list(map(int, input().split()))
    u1, v1 = list(map(int, input().split()))
    solve(n, m, a1, u1, v1)


# 10 8 12345
# 3 9
#
# 5 3 1565158
