def position(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return float("-inf")
    else:
        return arr_num_coins[i][j]


def solve(n, m, arr_num_coins):
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            else:
                arr_num_coins[i][j] += max(position(i - 1, j), position(i, j - 1))
    steps = []
    j = m - 1
    i = n - 1
    while j > 0 or i > 0:
        if position(i - 1, j) < position(i, j - 1):
            steps.append("R")
            j -= 1
        else:
            steps.append("D")
            i -= 1
    steps.reverse()
    steps_str = "".join(steps)

    return arr_num_coins[n - 1][m - 1], steps_str


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr_num_coins = []
    for i in range(n):
        arr_num_coins.append(list(map(int, input().split())))
    coins, path = solve(n, m, arr_num_coins)
    print(coins)
    print(path)



# 3 3
# 0 2 -3
# 2 -5 7
# 1 2 0
#
# 6
# RRDD

# 4 5
# 4 5 3 2 9
# 4 6 7 5 9
# 5 2 5 -3 -10
# 3 5 2 9 3
#
# 41
# RDRDDRR