import sys


class Fenwick:
    def __init__(self, input_lst, n):
        self.size = n
        self.f = [i & i + 1 for i in range(self.size)]
        self.t = [0] * self.size
        self.data = input_lst
        for i in range(self.size):
            for j in range(self.f[i], i + 1):
                self.t[i] += self.data[j]

    def get(self, idx):
        res = 0
        index = idx - 1
        while index >= 0:
            res += self.t[index]
            index = self.f[index] - 1
        return res

    def rsq(self, i, j):
        if i == 1:
            return Fenwick.get(self, j)
        return Fenwick.get(self, j) - Fenwick.get(self, i - 1)

    def set(self, i, x):
        idx = i - 1
        d = x - self.data[idx]
        self.data[idx] = x
        while idx < self.size:
            self.t[idx] += d
            idx = idx | (idx + 1)


def solve():
    n = int(sys.stdin.readline())
    input_lst = list(map(int, sys.stdin.readline().split()))
    f = Fenwick(input_lst, n)
    result_lst = []
    while True:
        command = sys.stdin.readline().split()
        if command == []:
            break
        elif command[0] == "sum":
            result_lst.append(str(f.rsq(int(command[1]), int(command[2]))))
        elif command[0] == "set":
            f.set(int(command[1]), int(command[2]))
    for i in result_lst:
        print(i)


if __name__ == "__main__":
    solve()

# 5
# 1 2 3 4 5
# sum 2 5
# sum 1 5
# sum 1 4
# sum 2 4
# set 1 10
# set 2 3
# set 5 2
# sum 2 5
# sum 1 5
# sum 1 4
# sum 2 4
#
# 14
# 15
# 10
# 9
# 12
# 22
# 20
# 10
