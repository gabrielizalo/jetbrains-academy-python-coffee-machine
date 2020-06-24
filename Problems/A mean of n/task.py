count = int(input())
numbers_list = []

for _x in range(count):
    numbers_list.append(int(input()))

sum_numbers = 0
count_numbers = len(numbers_list)
for x in numbers_list:
    sum_numbers += x
mean = sum_numbers / count_numbers
print(mean)
