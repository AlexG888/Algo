def heap(nums, heap_size, root_index):
    largest = root_index
    left_element = (2 * root_index) + 1
    right_element = (2 * root_index) + 2
    if left_element < heap_size and nums[left_element] > nums[largest]:
        largest = left_element
    if right_element < heap_size and nums[right_element] > nums[largest]:
        largest = right_element
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heap(nums, heap_size, largest)


def heap_sort(nums):
    for i in range(num_of_elements, -1, -1):
        heap(nums, num_of_elements, i)
    for i in range(num_of_elements - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heap(nums, i, 0)


num_of_elements = int(input())
list_of_nums = list(map(int, input().split()))
heap_sort(list_of_nums)
print(*list_of_nums)


# 10
# 1 8 2 1 4 7 3 2 3 6
#
# 1 1 2 2 3 3 4 6 7 8 