import sys

from random import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.priority = random()


class Balanced_binary_search_tree:
    def __init__(self):
        self.root = None

    def search(self, value):
        if self.root is not None:
            return self.search_body(value, self.root)
        else:
            return "false"

    def search_body(self, value, cur_node):
        if value == cur_node.value:
            return "true"
        elif value < cur_node.value and cur_node.left is not None:
            return self.search_body(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self.search_body(value, cur_node.right)
        return "false"

    @staticmethod
    def next(root, value):
        result = None
        while root is not None:
            if root.value > value:
                result = root
                root = root.left
            else:
                root = root.right
        if result is None:
            return "none"
        return str(result.value)

    @staticmethod
    def prev(root, value):
        result = None
        while root is not None:
            if root.value < value:
                result = root
                root = root.right
            else:
                root = root.left
        if result is None:
            return "none"
        return str(result.value)

    def split(self, root, value):
        if root is None:
            return None, None
        elif root.value is None:
            return None, None
        else:
            if value < root.value:
                left, root.left = self.split(root.left, value)
                return left, root
            else:
                root.right, right = self.split(root.right, value)
                return root, right

    def merge(self, left, right):
        if (not left) or (not right):
            return left or right
        elif left.priority < right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    def insert(self, root, value):
        node = Node(value)
        left, right = self.split(root, value)
        return self.merge(self.merge(left, node), right)

    def delete(self, root, value):
        left, right = self.split(root, value - 1)
        _, right = self.split(right, value)
        return self.merge(left, right)


t = Balanced_binary_search_tree()

for line in sys.stdin:
    command = list(line.split())
    if command[0] == "insert":
        t.root = t.insert(t.root, int(command[1]))
    elif command[0] == "delete":
        t.root = t.delete(t.root, int(command[1]))
    elif command[0] == "exists":
        print(t.search(int(command[1])))
    elif command[0] == "next":
        print(t.next(t.root, int(command[1])))
    elif command[0] == "prev":
        print(t.prev(t.root, int(command[1])))

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
