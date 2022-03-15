def merge_and_count_inversion(first_list, second_list):
    result = []
    i = j = count_inver = 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            result.append(first_list[i])
            i += 1
        else:
            result.append(second_list[j])
            count_inver += len(first_list) - i
            j += 1
    result += first_list[i:]
    result += second_list[j:]
    return result, count_inver


def merge_sort(nums):
    if len(nums) == 1:
        return nums, 0
    middle = len(nums) // 2
    left, c1 = merge_sort(nums[:middle])
    right, c2 = merge_sort(nums[middle:])
    res, c3 = merge_and_count_inversion(left, right)
    return res, (c1 + c2 + c3)


num_of_elements = int(input())
list_of_nums = list(map(int, input().split()))
print(merge_sort(list_of_nums)[1])

# 4
# 1 2 4 5
#
# 0