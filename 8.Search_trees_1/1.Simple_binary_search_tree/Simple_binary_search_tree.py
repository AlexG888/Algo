import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
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
        elif v.right is None and v.left is None:
            v = None
        elif v.left is None:
            v = v.right
        elif v.right is None:
            v = v.left
        else:
            v.key = self.find_max(v.left).key
            v.left = self.delete(v.key, v.left)
        return v

    def find_max(self, v):
        while v.right is not None:
            v = v.right
        return v

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


def solve():
    t = BinarySearchTree()
    lines = sys.stdin.readlines()
    commands = [line.split() for line in lines]
    for command in commands:
        if command[0] == "insert":
            t.insert(int(command[1]))
        elif command[0] == "delete":
            t.delete(int(command[1]))
        elif command[0] == "exists":
            print(t.exists(int(command[1])))
        elif command[0] == "next":
            print(t.next(int(command[1])))
        elif command[0] == "prev":
            print(t.prev(int(command[1])))


if __name__ == "__main__":
    solve()


# insert 2
# insert 5
# insert 3
# exists 2
# exists 4
# next 4
# prev 4
# delete 5
# next 4
# prev 4
#
# true
# false
# 5
# 3
# none
# 3
