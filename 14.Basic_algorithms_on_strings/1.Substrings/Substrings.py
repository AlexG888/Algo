class Hash_string:
    def __init__(self):
        self.p = 29
        self.mod = 10 ** 8 + 3
        self.powp = [1]
        self.hash_arr = [0]
 
    def hash_string(self, s):
        self.hash_arr[0] = ord(s[0]) - ord("a") + 1
        for i in range(1, len(s)):
            x = ord(s[i]) - ord("a") + 1
            self.powp.append((self.powp[i - 1] * self.p) % self.mod)
            self.hash_arr.append((self.hash_arr[i - 1] * self.p + x) % self.mod)
 
    def get_hash(self, left, right):
        if left == 0:
            return self.hash_arr[right]
        return (
            self.hash_arr[right]
            - (self.hash_arr[left - 1] * self.powp[right - left + 1]) % self.mod
            + self.mod
        ) % self.mod
 
 
if __name__ == "__main__":
    s = input()
    hs = Hash_string()
    hs.hash_string(s)
    m = int(input())
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        hash_one = hs.get_hash(a - 1, b - 1)
        hash_two = hs.get_hash(c - 1, d - 1)
        print("Yes" if hash_one == hash_two else "No")


# trololo
# 3
# 1 7 1 7
# 3 5 5 7
# 1 1 1 5

# Yes
# Yes
# No