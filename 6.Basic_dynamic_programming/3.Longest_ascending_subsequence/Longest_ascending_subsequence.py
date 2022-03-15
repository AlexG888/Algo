def solve(arr_elements, n):
    dp = [0] * n
    for i in range(n):
        for j in range(i):
            if arr_elements[i] > arr_elements[j] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] += 1

    answer = max(dp)
    i = dp.index(answer)
    subsequence = [arr_elements[i]]

    while dp[i] != 1:
        j = i - 1
        while dp[j] + 1 != dp[i] or arr_elements[j] >= arr_elements[i]:
            j -= 1
        i = j
        subsequence.append(arr_elements[i])
    return answer, subsequence


if __name__ == "__main__":
    n = int(input())
    arr_elements = list(map(int, input().split()))
    k, subsequence = solve(arr_elements, n)
    print(k)
    print(" ".join(map(str, subsequence[::-1])))


# 8
# 1 4 1 5 3 3 4 2

# 3
# 1 4 5

# 3
# 1 2 3

# 3
# 1 2 3
