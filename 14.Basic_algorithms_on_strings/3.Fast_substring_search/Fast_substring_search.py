def kmp(t, p):
    s = p + "#" + t
    p_arr = [0] * len(s)
    for i in range(1, len(s)):
        k = p_arr[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p_arr[k - 1]
        if s[k] == s[i]:
            k += 1
        p_arr[i] = k
    return p_arr


if __name__ == "__main__":
    p = input()
    t = input()
    kmp = kmp(t, p)
    result = []
    for i in range(len(kmp)):
        if kmp[i] == len(p):
            result.append(i + 1 - 2 * len(p))
    print(len(result))
    print(*result)

# aba
# abaCaba
#
# 2
# 1 5