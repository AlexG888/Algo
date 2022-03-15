from IPython import embed

def solve(n, k, arr_num_coins):
    arr_num_coins = [0] + arr_num_coins + [0]
    dp = [0] * n
    p = [None] * n

    for i in range(1, n):
        max_i = i - 1
        j = max(0, i - k)
        while j < i:
            if dp[j] > dp[max_i]:
                max_i = j
            j += 1
        dp[i] = dp[max_i] + arr_num_coins[i]
        p[i] = max_i

    steps = []
    i = n - 1
    steps.append(str(i + 1))
    while i > 0:
        steps.append(str(p[i] + 1))
        i = p[i]
    steps.reverse()
    embed()
    return dp[n - 1], steps


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr_num_coins = list(map(int, input().split()))
    max_coins, steps = solve(n, k, arr_num_coins)
    print(max_coins)
    print(len(steps) - 1)
    print(" ".join(map(str, steps)))


# 5 3
# 2 -3 5
#
# 7
# 3
# 1 2 4 5

# 10 3
# -13 -2 -14 -124 -9 -6 -5 -7
#
# -16
# 4
# 1 3 6 8 10

# 12 5
# -5 -4 -3 -2 -1 1 2 3 4 5
#
# 14
# 7
# 1 6 7 8 9 10 11 12