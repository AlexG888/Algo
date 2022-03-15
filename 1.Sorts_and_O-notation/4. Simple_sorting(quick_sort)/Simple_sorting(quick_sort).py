import random


def swap(list_of_nums, i, j):
    list_of_nums[i], list_of_nums[j] = list_of_nums[j], list_of_nums[i]


def partition(list_of_nums, first, last):
    rand = random.choice(list_of_nums[first:last])
    (i, j) = (first - 1, last + 1)
    while True:
        while True:
            i += 1
            if list_of_nums[i] >= rand:
                break
        while True:
            j -= 1
            if list_of_nums[j] <= rand:
                break
        if i >= j:
            return j
        swap(list_of_nums, i, j)


def sort(list_of_nums, first, last):
    if first >= last:
        return
    pivot = partition(list_of_nums, first, last)
    sort(list_of_nums, first, pivot)
    sort(list_of_nums, pivot + 1, last)


def quick_sort(list_of_nums):
    sort(list_of_nums, 0, len(list_of_nums) - 1)


if __name__ == "__main__":
    num_of_elements = int(input())
    list_of_nums = list(map(int, input().split()))
    quick_sort(list_of_nums)
    print(*list_of_nums)

# 10
# 1 8 2 1 4 7 3 2 3 6
#
# 1 1 2 2 3 3 4 6 7 8 