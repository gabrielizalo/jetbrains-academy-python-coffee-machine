# User Data
number_a = int(input())
number_b = int(input())
numbers_list = []

# Create number list divided by 3
for i in range(number_a, number_b + 1):
    if i % 3 == 0:
        numbers_list.append(i)

# Calculate mean
sum_numbers = 0
for i in numbers_list:
    sum_numbers += i
mean = sum_numbers / len(numbers_list)
print(mean)
