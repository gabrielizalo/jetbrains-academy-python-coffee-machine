digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
user_number = input()

for char in user_number:
    print(digits[int(char)])
