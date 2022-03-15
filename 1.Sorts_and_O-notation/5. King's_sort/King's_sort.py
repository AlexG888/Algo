import random


def swap(list_of_elem, i, j):
    list_of_elem[i], list_of_elem[j] = list_of_elem[j], list_of_elem[i]


def partition(list_of_elem, first, last):
    rand = random.choice(list_of_elem[first:last])
    (i, j) = (first - 1, last + 1)
    while True:
        while True:
            i += 1
            if list_of_elem[i] >= rand:
                break
        while True:
            j -= 1
            if list_of_elem[j] <= rand:
                break
        if i >= j:
            return j
        swap(list_of_elem, i, j)


def sort(list_of_elem, first, last):
    if first >= last:
        return
    pivot = partition(list_of_elem, first, last)
    sort(list_of_elem, first, pivot)
    sort(list_of_elem, pivot + 1, last)


def quick_sort(list_of_elem):
    sort(list_of_elem, 0, len(list_of_elem) - 1)


def roman_numerals_to_int(roman_num):
    dictionary = {"L": 50, "X": 10, "V": 5, "I": 1}
    n = [dictionary[i] for i in roman_num if i in dictionary]
    return sum([i if i >= n[min(j + 1, len(n) - 1)] else -i for j, i in enumerate(n)])


def kings_sort(list_of_kings):
    for i in list_of_kings:
        i.append(i[1])
        i[1] = roman_numerals_to_int(i[1])
    quick_sort(list_of_kings)


if __name__ == "__main__":
    num_of_kings = int(input())
    list_of_kings = [list(map(str, input().split())) for _ in range(num_of_kings)]
    kings_sort(list_of_kings)
    for i in list_of_kings:
        print(*i[0:3:2])


# 2
# Louis IX
# Louis VIII
#
# Louis VIII
# Louis IX