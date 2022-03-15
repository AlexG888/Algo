def merge_two_lists(first_list, second_list):
    result = []
    i = j = 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            result.append(first_list[i])
            i += 1
        else:
            result.append(second_list[j])
            j += 1
    if i < len(first_list):
        result += first_list[i:]
    if j < len(second_list):
        result += second_list[j:]
    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge_two_lists(left, right)


num_of_elements = int(input())
list_of_nums = list(map(int, input().split()))
print(*merge_sort(list_of_nums))

# 10
# 1 8 2 1 4 7 3 2 3 6
#
# 1 1 2 2 3 3 4 6 7 8 