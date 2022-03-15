def solve(string1, string2):
    len_str1, len_str2 = len(string1), len(string2)
    if len_str1 > len_str2:
        string1, string2 = string2, string1
        len_str1, len_str2 = len_str2, len_str1

    dp = [i for i in range(len_str1 + 1)]
    for i in range(1, len_str2 + 1):
        prev, dp = dp, [i] + [0] * len_str1
        for j in range(1, len_str1 + 1):
            add, delete, change = prev[j] + 1, dp[j - 1] + 1, prev[j - 1]
            if string1[j - 1] != string2[i - 1]:
                change += 1
            dp[j] = min(add, delete, change)

    return dp[len_str1]


if __name__ == "__main__":
    string1 = input()
    string2 = input()
    print(solve(string1, string2))


# ABCDEFGH
# ACDEXGIH

# 3


