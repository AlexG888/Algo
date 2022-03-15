import ctypes
import sys


class Stack:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def push(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1

    def resize(self, new_cap):
        new_array = self.make_array(new_cap)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def pop(self):
        if self.size:
            if 0 < self.size <= self.capacity / 4:
                self.new_cap = self.size
                self.resize(self.new_cap)
            self.size = self.size - 1
            return self.array[self.size]


def solve(lst):
    s = Stack()
    for i in lst:
        if i.isdigit():
            s.push(int(i))
            continue
        y = s.pop()
        x = s.pop()
        oper = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }[i](x, y)
        s.push(oper)
    return s.pop()


if __name__ == "__main__":
    lst = sys.stdin.readline().split()
    print(solve(lst))

# 8 9 + 1 7 - *
#
# -102