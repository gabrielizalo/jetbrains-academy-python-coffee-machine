number_user = input()
min_number = 1000000

while number_user != '.':
    float_number = float(number_user)
    if float_number < min_number:
        min_number = float_number
    number_user = input()

print(min_number)
