from sre_constants import OP_LOCALE_IGNORE
from tkinter.messagebox import NO


class Trie:
    def __init__(self):
        self.size = 1
        self.next = [dict()]
        self.isTerminal = [-1]
 
    def insert(self, s, n):
        v = 0
        for sym in s:
            if sym not in self.next[v].keys():
                self.next[v][sym] = self.size
                self.next.append(dict())
                self.isTerminal.append(-1)
                self.size += 1
            v = self.next[v][sym]
        self.isTerminal[v] = n
 
    def contains(self, s):
        v = 0
        cont = []
        for sym in s:
            if sym not in self.next[v].keys():
                return cont
            if self.isTerminal[self.next[v][sym]] != -1:
                cont.append(self.isTerminal[self.next[v][sym]])
            v = self.next[v][sym]
        return cont
 
 
MAX_LEN = 30
 
if __name__ == "__main__":
    t = Trie()
    s = input()
    m = int(input())
    result = ["No" for _ in range(m)]
    for i in range(m):
        t.insert(input(), i)
    for i in range(len(s)):
        for idx in t.contains(s[i : i + MAX_LEN]):
            result[idx] = "Yes"
    print("\n".join(result))


# trololo
# 3
# abacabadabacaba
# olo
# trol
#
# No
# Yes
# Yes