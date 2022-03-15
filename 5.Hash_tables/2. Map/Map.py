import sys
from math import sqrt


class HashMap:
    def __init__(self):
        self.map = [None] * SIZE

    def _get_hash(self, key):
        res = 0
        for char in str(key):
            res += res * A + ord(char) - 96
        return res % SIZE

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return print(pair[1])
        return print("none")

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False


A = 31
SIZE = int(sqrt(100000))

h = HashMap()
while True:
    command = sys.stdin.readline().split()
    if command == []:
        break
    elif command[0] == "put":
        h.add(command[1], command[2])
    elif command[0] == "get":
        h.get(command[1])
    elif command[0] == "delete":
        h.delete(command[1])


# put hello privet
# put bye poka
# get hello
# get bye
# delete hello
# get hello
#
# privet
# poka
# none

