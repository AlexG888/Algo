import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())
    first_list = list(map(int, sys.stdin.readline().split()))
    second_list = list(map(int, sys.stdin.readline().split()))

    for i in second_list:
        left = 0
        right = n - 1
        while right - left > 1:
            middle = (right + left) // 2
            if first_list[middle] < i:
                left = middle
            else:
                right = middle
        if i - first_list[left] <= first_list[right] - i:
            print(first_list[left])
        else:
            print(first_list[right])


if __name__ == "__main__":
    solve()

# 5 5
# 1 3 5 7 9
# 2 4 8 1 6
# 
# 1
# 3
# 7
# 1
# 5