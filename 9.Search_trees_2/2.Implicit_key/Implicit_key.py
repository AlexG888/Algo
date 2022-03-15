import sys

from random import random


class Node:
    def __init__(self, x):
        self.x = x
        self.size = 1
        self.left = None
        self.right = None
        self.priority = random()


class Balanced_binary_search_tree:
    def __init__(self):
        self.root = None
        self.arr = []
        self.num = 0

    def get_size(self, root):
        if root is None:
            return 0
        else:
            return root.size

    def fix_size(self, root):
        root.size = self.get_size(root.left) + self.get_size(root.right) + 1

    def split(self, root, value):
        if root is None:
            return None, None
        else:
            if self.get_size(root.left) > value:
                left, root.left = self.split(root.left, value)
                self.fix_size(root)
                return left, root
            else:
                root.right, right = self.split(
                    root.right, value - self.get_size(root.left) - 1
                )
                self.fix_size(root)
                return root, right

    def merge(self, left, right):
        if (not left) or (not right):
            return left or right
        elif left.priority < right.priority:
            left.right = self.merge(left.right, right)
            self.fix_size(left)
            return left
        else:
            right.left = self.merge(left, right.left)
            self.fix_size(right)
            return right

    def insert(self, root, value, x):
        node = Node(x)
        left, right = self.split(root, value)
        return self.merge(self.merge(left, node), right)

    def delete(self, root, value):
        left, right = self.split(root, value)
        t11, t12 = self.split(left, value - 1)
        left = self.merge(t11, right)
        return left

    def load_values(self):
        if self.root is not None:
            self.arr = [0 for _ in range(self.get_size(self.root))]
            self.load(self.root)

    def load(self, root):
        if root is not None:
            if root.left is not None:
                self.load(root.left)
            self.arr[self.num] = str(root.x)
            self.num += 1
            self.load(root.right)


n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

t = Balanced_binary_search_tree()

for i in range(n):
    t.root = t.insert(t.root, i, array[i])
for line in sys.stdin.read().splitlines():
    command = list(line.split())
    if command == []:
        break
    elif command[0] == "add":
        t.root = t.insert(t.root, int(command[1]) - 1, int(command[2]))
    elif command[0] == "del":
        t.root = t.delete(t.root, int(command[1]) - 1)

print(t.get_size(t.root))
t.load_values()
print(" ".join(t.arr))


# 3 4
# 1 2 3
# del 3
# add 0 9
# add 3 8
# del 2
#
# 3
# 9 2 8
