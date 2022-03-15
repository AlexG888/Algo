def solve(n, arr_prices):
    dp = [[0 for _ in range(n + 3)] for _ in range(n + 1)]
    prev = [[None for _ in range(n + 3)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = INF
        dp[i][n + 2] = INF
    for j in range(2, n + 3):
        dp[0][j] = INF
    for i in range(1, n + 1):
        for j in range(n + 1, 0, -1):
            if arr_prices[i - 1] <= MIN_PRICE:
                if dp[i - 1][j] + arr_prices[i - 1] < dp[i - 1][j + 1]:
                    dp[i][j] = dp[i - 1][j] + arr_prices[i - 1]
                    prev[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j + 1]
                    prev[i][j] = -1
            else:
                if dp[i - 1][j - 1] + arr_prices[i - 1] < dp[i - 1][j + 1]:
                    dp[i][j] = dp[i - 1][j - 1] + arr_prices[i - 1]
                    prev[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j + 1]
                    prev[i][j] = -1
    min_cost = dp[n][n + 2]
    num_not_used_coupons = n + 2
    for j in range(n + 1, 0, -1):
        if dp[n][j] < min_cost:
            min_cost = dp[n][j]
            num_not_used_coupons = j - 1
    used_coupons = []
    num_coupons = num_not_used_coupons
    for i in range(n, 0, -1):
        if prev[i][num_coupons + 1] == 1:
            num_coupons -= 1
        elif prev[i][num_coupons + 1] == -1:
            num_coupons += 1
            used_coupons.append(i)
    used_coupons.reverse()
    return (min_cost, num_not_used_coupons, used_coupons)


INF = float("inf")
MIN_PRICE = 100

if __name__ == "__main__":
    n = int(input())
    arr_prices = []
    for i in range(n):
        arr_prices.append(int(input()))
    min_cost, num_not_used_coupons, used_coupons = solve(n, arr_prices)
    num_used_coupons = len(used_coupons)
    print(min_cost)
    print(num_not_used_coupons, num_used_coupons)
    for k in range(num_used_coupons):
        print(used_coupons[k])


# 5
# 110
# 40
# 120
# 110
# 60
#
# 260
# 0 2
# 3
# 5

# 3
# 110
# 110
# 110
#
# 220
# 1 1
# 2
