class Tree:
    def __init__(self, n):
        self.size = n
        self.min_tree = [MAX_VAL] * (2 ** (self.power() + 1) - 1)
        self.labels_list = [None] * len(self.min_tree)
        self.num_leaves = 2 ** self.power()

    def power(self):
        if self.size == 1:
            return 0
        else:
            log2arr = [0] * (self.size)
            for i in range(2, self.size):
                log2arr[i] = log2arr[i - 1]
                if (1 << (log2arr[i] + 1)) <= i:
                    log2arr[i] += 1
            power2arr = [0] + [i + 1 for i in range(log2arr[-1] + 1)]
            return power2arr[-1]

    def push(self, i, left_i, right_i):
        if right_i - left_i == 1 or self.labels_list[i] is None:
            return
        self.min_tree[2 * i + 1] = self.min_tree[2 * i + 2] = self.labels_list[i]
        self.labels_list[2 * i + 1] = self.labels_list[2 * i + 2] = self.labels_list[i]
        self.labels_list[i] = None

    def get_min(self, i, left, right, left_i, right_i):
        self.push(i, left_i, right_i)
        if left_i >= left and right_i <= right:
            return self.min_tree[i]
        elif left >= right_i or left_i >= right:
            return MAX_VAL
        m = (left_i + right_i) / 2
        m_left = self.get_min(2 * i + 1, left, right, left_i, m)
        m_right = self.get_min(2 * i + 2, left, right, m, right_i)
        return min(m_left, m_right)

    def set(self, i, x, left, right, left_i, right_i):
        self.push(i, left_i, right_i)
        if left >= right_i or left_i >= right:
            return
        elif left_i >= left and right_i <= right:
            self.labels_list[i] = self.min_tree[i] = x
            return
        m = (left_i + right_i) / 2
        self.set(2 * i + 1, x, left, right, left_i, m)
        self.set(2 * i + 2, x, left, right, m, right_i)
        self.min_tree[i] = min(self.min_tree[2 * i + 1], self.min_tree[2 * i + 2])


MAX_VAL = 2 ** 31 - 1

if __name__ == "__main__":
    q_list = []
    with open("rmq.in") as in_f:
        n, m = map(int, in_f.readline().split())
        for line in in_f.readlines():
            i, j, q = map(int, line.split())
            q_list.append((i, j, q))
    q_list = sorted(q_list, key=lambda i: i[2])
    t = Tree(n)
    for i, j, q in q_list:
        t.set(0, q, i - 1, j, 0, t.num_leaves)
    condition = None
    for i, j, q in q_list:
        if t.get_min(0, i - 1, j, 0, t.num_leaves) != q:
            condition = "inconsistent"
            break
    with open(
        "rmq.out",
        "w",
    ) as out_f:
        if condition is not None:
            out_f.write(condition)
        else:
            for i in range(2 ** t.power() - 1):
                t.push(i, 0, 2)
            result = t.min_tree[2 ** t.power() - 1 : 2 ** t.power() + n - 1]
            out_f.write(f'consistent\n{" ".join(map(str, result))}')

# 3 2
# 1 2 1
# 2 3 2
#
# consistent
# 1 2 2

# 3 3
# 1 2 1
# 1 1 2
# 2 3 2
#
# inconsistent