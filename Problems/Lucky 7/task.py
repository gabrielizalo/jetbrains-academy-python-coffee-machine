import itertools

n = int(input())
list_numbers = []
for _ in itertools.repeat(None, n):
    list_numbers.append(int(input()))

for number in list_numbers:
    if number % 7 == 0:
        print(number * number)
