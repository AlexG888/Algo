def counting_sort(list_of_str, position):
    support = [0 for i in range(AMOUT_OF_SYMBOLS)]
    for string in list_of_str:
        support[ord(string[position]) - ord("a")] += 1
    size = len(list_of_str)
    for i in range(AMOUT_OF_SYMBOLS - 1, -1, -1):
        size -= support[i]
        support[i] = size
    result = [None for i in range(len(list_of_str))]
    for string in list_of_str:
        result[support[ord(string[position]) - ord("a")]] = string
        support[ord(string[position]) - ord("a")] += 1
    return result


def radix_sort(list_of_str):
    for i in range(1, k + 1):
        list_of_str = counting_sort(list_of_str, -i)
    return list_of_str


AMOUT_OF_SYMBOLS = 26

inp = list(map(int, input().split()))
m = inp[1]  # length
k = inp[2]
list_of_str = []
for i in range(inp[0]):
    list_of_str.append(input())
for j in radix_sort(list_of_str):
    print(j)


# 3 3 1
# bbb
# aba
# baa
#
# aba
# baa
# bbb