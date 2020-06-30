user_number = int(input())
sum_numbers = user_number
numbers = [sum_numbers]

while sum_numbers != 0 and len(numbers) > 0:
    user_number = int(input())
    sum_numbers = sum_numbers + user_number
    numbers.append(user_number)

sum_squares = 0
for i in numbers:
    sum_squares = sum_squares + i * i

print(sum_squares)
