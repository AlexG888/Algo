MAX_VAL = 101

list_of_nums = list(map(int, input().split()))
amount_of_numbers = [0] * MAX_VAL
for i in list_of_nums:
    amount_of_numbers[i] += 1
for j in range(len(amount_of_numbers)):
    for q in range(amount_of_numbers[j]):
        print(j, end=" ")

# 7 3 4 2 5
#
# 2 3 4 5 7