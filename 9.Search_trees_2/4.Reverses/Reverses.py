import sys

from random import randint

MAX_PRIORITY = 10 ** 5


class Node:
    def __init__(self, value, count, priority):
        self.left = None
        self.right = None
        self.reversed = False
        self.value = value
        self.count = count
        self.priority = priority


class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_count(self, root):
        if root is not None:
            return root.count
        else:
            return 0

    def fix_count(self, root):
        return self.get_count(root.left) + self.get_count(root.right) + 1

    def swap(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp
        root.reversed = False
        if self.get_count(root.left) > 1:
            root.left.reversed = not root.left.reversed
        if self.get_count(root.right) > 1:
            root.right.reversed = not root.right.reversed
        return root

    def split(self, root, value):
        if root is None:
            return None, None
        if root.reversed:
            root = self.swap(root)
        if self.get_count(root.left) > value:
            tree_left, tree_right = self.split(root.left, value)
            root.left = tree_right
            root.count = self.fix_count(root)
            return tree_left, root
        else:
            tree_left, tree_right = self.split(
                root.right, value - self.get_count(root.left) - 1
            )
            root.right = tree_left
            root.count = self.fix_count(root)
            return root, tree_right

    def merge(self, tree_left, tree_right):
        if tree_left is None:
            return tree_right
        if tree_left.reversed:
            tree_left = self.swap(tree_left)
        if tree_right is None:
            return tree_left
        if tree_right.reversed:
            tree_right = self.swap(tree_right)
        if tree_left.priority > tree_right.priority:
            tree_left.right = self.merge(tree_left.right, tree_right)
            tree_left.count = self.fix_count(tree_left)
            if tree_left.reversed:
                tree_left = self.swap(tree_left)
            return tree_left
        else:
            tree_right.left = self.merge(tree_left, tree_right.left)
            tree_right.count = self.fix_count(tree_right)
            return tree_right

    def insert(self, root, value, idx, priority):
        tree_left, tree_right = self.split(root, idx)
        new_node = Node(value, 1, priority)
        tree_left = self.merge(tree_left, new_node)
        return self.merge(tree_left, tree_right)

    def reverse(self, root, left, right):
        tree_left, tree_right = self.split(root, right)
        tree_left_left, tree_left_right = self.split(tree_left, left - 1)
        if tree_left_right.reversed == False and tree_left_right is not None:
            tree_left_right = self.swap(tree_left_right)
        tree_left = self.merge(tree_left_left, tree_left_right)
        return self.merge(tree_left, tree_right)


n, m = map(int, sys.stdin.readline().strip().split())
t = Tree()
for i in range(n):
    t = Tree(t.insert(t.root, i + 1, i, randint(0, MAX_PRIORITY)))
for line in sys.stdin.readlines():
    l, r = map(int, line.strip().split())
    t = Tree(t.reverse(t.root, l - 1, r - 1))
while True:
    t1, t2 = t.split(t.root, 0)
    t = Tree(root=t2)
    if t1 is not None:
        print(str(t1.value), end=" ")
    else:
        break


# 5 3
# 2 4
# 3 5
# 2 2
#
# 1 4 5 2 3
