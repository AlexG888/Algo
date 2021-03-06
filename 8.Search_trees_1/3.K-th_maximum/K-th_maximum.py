import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1
        self.m = 0


class AVL_BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, x, v="root"):
        if v == "root":
            if self.root is None:
                self.root = Node(x)
                return self.root
            return self.insert(x, self.root)
        if v is None:
            return Node(x)
        elif x < v.key:
            v.left = self.insert(x, v.left)
        elif x > v.key:
            v.right = self.insert(x, v.right)
        return self.balance(v)

    def fix(self, v):
        if v.right is None and v.left is None:
            v.h = 1
            v.m = 0
        elif v.left is None:
            v.h = v.right.h + 1
            v.m = v.right.m + 1
        elif v.right is None:
            v.h = v.left.h + 1
            v.m = v.left.m + 1
        else:
            v.h = max(v.left.h, v.right.h) + 1
            v.m = v.left.m + v.right.m + 2

    def node_balance(self, v):
        if v.right is None and v.left is None:
            return 0
        elif v.left is None:
            return v.right.h
        elif v.right is None:
            return 0 - v.left.h
        else:
            return v.right.h - v.left.h

    def balance(self, v):
        if v is None:
            return v
        self.fix(v)
        b = self.node_balance(v)
        if b == 2:
            if self.node_balance(v.right) < 0:
                v.right = self.small_rotate(v.right, "right")
            return self.small_rotate(v, "left")
        elif b == -2:
            if self.node_balance(v.left) > 0:
                v.left = self.small_rotate(v.left, "left")
            return self.small_rotate(v, "right")
        return v

    def small_rotate(self, p, how):
        if how == "right":
            q = p.left
            p.left = q.right
            q.right = p
        else:
            q = p.right
            p.right = q.left
            q.left = p
        if q.left == self.root or q.right == self.root:
            self.root = q
        self.fix(p)
        self.fix(q)
        return q

    def delete(self, x, v="root"):
        if v == "root":
            if self.root is None:
                return self.root
            self.root = self.delete(x, self.root)
            return
        if v is None:
            return None
        if x < v.key:
            v.left = self.delete(x, v.left)
        elif x > v.key:
            v.right = self.delete(x, v.right)
        elif v.left is None:
            v = v.right
        elif v.right is None:
            v = v.left
        else:
            v.key = self.find_max(v.left).key
            v.left = self.delete(v.key, v.left)
        return self.balance(v)

    def find_max(self, v):
        while v.right is not None:
            v = v.right
        return v

    def exists(self, x, v="root"):
        if v == "root":
            if self.root is None:
                return "false"
            return self.exists(x, self.root)
        if v is None:
            return "false"
        if v.key == x:
            return "true"
        elif x < v.key:
            return self.exists(x, v.left)
        else:
            return self.exists(x, v.right)

    def next(self, x):
        if self.root is None:
            return "none"
        v = self.root
        next_key = "none"
        while v is not None:
            if v.key > x:
                next_key = v.key
                v = v.left
            else:
                v = v.right
        return next_key

    def prev(self, x):
        if self.root is None:
            return "none"
        v = self.root
        prev_key = "none"
        while v is not None:
            if v.key < x:
                prev_key = v.key
                v = v.right
            else:
                v = v.left
        return prev_key

    def kmax(self, k, v="root"):
        if v == "root":
            return self.kmax(k, self.root)
        if v.left is None:
            m_left = 0
        else:
            m_left = v.left.m + 1
        if v.right is None:
            m_right = 0
        else:
            m_right = v.right.m + 1
        cnt = m_left + 1 + m_right
        if cnt - k < m_left:
            return self.kmax(k - m_right - 1, v.left)
        elif k < m_right + 1:
            return self.kmax(k, v.right)
        else:
            return v.key


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    commands = [line.split() for line in lines]
    t = AVL_BinarySearchTree()
    n = commands[0][0]
    for command in commands[1:]:
        x = int(command[1])
        if command[0] == "+1" or command[0] == "1":
            t.insert(x)
        elif command[0] == "0":
            print(t.kmax(x))
        else:
            t.delete(x)


# 11
# +1 5
# +1 3
# +1 7
# 0 1
# 0 2
# 0 3
# -1 5
# +1 10
# 0 1
# 0 2
# 0 3
#
# 7
# 5
# 3
# 10
# 7
# 3
