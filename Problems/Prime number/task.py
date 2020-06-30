def is_prime(number):
    if number == 1:
        return False

    i = 2
    seems_prime = True
    while seems_prime and i < number:
        if number % i == 0:
            seems_prime = False
        i = i + 1
    return seems_prime


user_number = int(input())
if is_prime(user_number):
    print('This number is prime')
else:
    print('This number is not prime')
