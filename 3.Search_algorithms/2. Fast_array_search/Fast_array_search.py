import sys


def amount_of_elements(num_list, edge_element, n):
    left = -1
    right = n
    while left + 1 < right:
        middle = (right + left) // 2
        if num_list[middle] <= edge_element:
            left = middle
        else:
            right = middle
    return left


def solve():
    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.sort()
    k = int(sys.stdin.readline())
    pairs_list = []
    for _ in range(k):
        pairs_list.append(list(map(int, sys.stdin.readline().split())))
    for i in range(k):
        print(
            amount_of_elements(num_list, pairs_list[i][1], n)
            - amount_of_elements(num_list, pairs_list[i][0] - 1, n)
        )


if __name__ == "__main__":
    solve()


# 5
# 10 1 10 3 4
# 4
# 1 10
# 2 9
# 3 4
# 2 2
#
# 5 2 2 0