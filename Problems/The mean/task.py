user_number = input()
total = 0
quantity = 0
while user_number != '.':
    total += int(user_number)
    quantity += 1
    user_number = input()

mean = total / quantity
print(mean)
