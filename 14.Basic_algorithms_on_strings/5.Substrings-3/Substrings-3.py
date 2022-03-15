from collections import defaultdict


class Hash_string:
    DEF_P = 29
    DEF_M = 10 ** 8 + 3

    def __init__(self, string, p=DEF_P, m=DEF_M):
        self.string = string
        self.p = p
        self.m = m
        self.hashes = []
        self.powers = []
        self.hash_string()

    def hash_string(self):
        cur_hash = 0
        cur_p = 1
        for i in self.string:
            cur_hash = cur_hash * self.p + (ord(i) - ord("a") + 1)
            cur_hash %= self.m
            self.hashes.append(cur_hash)
            self.powers.append(cur_p)
            cur_p = (cur_p * self.p) % self.m

    def get_hash(self, left, right):
        if left == 0:
            return self.hashes[right]
        return (
            self.hashes[right] - self.hashes[left - 1] * self.powers[right - left + 1]
        ) % self.m

    def __len__(self):
        return len(self.string)


if __name__ == "__main__":
    k = int(input())
    strings = []
    for _ in range(k):
        strings.append(input())
    strings = list(map(Hash_string, sorted(strings, key=len)))
    min_len = len(strings[0])
    left, right = 1, min_len + 1
    lcs = None
    while left < right:
        middle = (right + left) // 2
        hashes = defaultdict(list)
        intersected_hashes = set()
        for idx, string in enumerate(strings):
            for i in range(len(string) - middle + 1):
                hashes[string].append(string.get_hash(i, i + middle - 1))
            if idx == 0:
                intersected_hashes = set(hashes[string])
            else:
                intersected_hashes = intersected_hashes.intersection(
                    set(hashes[string])
                )
                if len(intersected_hashes) == 0:
                    exists, res = False, []
        for i in range(len(hashes[string])):
            if hashes[string][i] in intersected_hashes:
                exists, res = True, string.string[i : i + middle]
        if not exists:
            right = middle
        else:
            lcs = res
            left = middle + 1
    print(lcs)

# 3
# abacaba
# mycabarchive
# acabistrue
#
# cab


