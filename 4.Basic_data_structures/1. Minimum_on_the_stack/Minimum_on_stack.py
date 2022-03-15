import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.min = float("inf")

    def push(self, x):
        if self.top == None:
            self.top = Node(x)
            self.min = x
        else:
            if x >= self.min:
                node = Node(x)
                node.next = self.top
                self.top = node
            else:
                val = 2 * x - self.min
                node = Node(val)
                node.next = self.top
                self.top = node
                self.min = x

    def pop(self):
        if self.top:
            if self.top.value < self.min:
                self.min = self.min * 2 - self.top.value
            self.top = self.top.next

    def get_min(self):
        if self.top:
            return print(self.min)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    s = Stack()
    for _ in range(n):
        k = str(sys.stdin.readline())
        if len(k) > 1 and int(k[0]) == 1:
            s.push(int(k[2:]))
        elif int(k) == 2:
            s.pop()
        elif int(k) == 3:
            s.get_min()


# 8
# 1 2
# 1 3
# 1 -3
# 3
# 2
# 3
# 2
# 3
#
# -3
# 2
# 2