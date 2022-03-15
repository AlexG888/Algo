def partition(list_of_nums, first, last, k):
    pos = first
    for i in range(first, last):
        if list_of_nums[i] < list_of_nums[last]:
            list_of_nums[i], list_of_nums[pos] = list_of_nums[pos], list_of_nums[i]
            pos += 1

    list_of_nums[pos], list_of_nums[last] = list_of_nums[last], list_of_nums[pos]
    return pos


def sort(list_of_nums, first, last, k):
    if first < last:
        pos = partition(list_of_nums, first, last, k)
        if pos >= k:
            sort(list_of_nums, first, pos - 1, k)
        else:
            sort(list_of_nums, pos + 1, last, k)


def kth(list_of_nums, list_of_requests):
    for request in list_of_requests:
        arr = list_of_nums[request[0] - 1 : request[1]]
        sort(arr, 0, len(arr) - 1, request[2])
        print(arr[request[2] - 1])


if __name__ == "__main__":
    n = int(input())
    list_of_nums = list(map(int, input().split()))
    m = int(input())
    list_of_requests = [list(map(int, input().split())) for _ in range(m)]
    kth(list_of_nums, list_of_requests)

# 5
# 1 3 2 4 5
# 3
# 1 3 2
# 1 5 1
# 1 5 2
#
# 2
# 1
# 2