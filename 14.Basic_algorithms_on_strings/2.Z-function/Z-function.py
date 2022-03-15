def zfunction(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


if __name__ == "__main__":
    s = input()
    print(*zfunction(s)[1:])

# aaaAAA
#
# 2 1 0 0 0

# abacaba
#
# 0 1 0 3 0 1