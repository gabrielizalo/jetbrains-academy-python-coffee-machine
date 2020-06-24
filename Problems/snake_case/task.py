lower_camel_case = input()
snake_case = ""
for char in lower_camel_case:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
print(snake_case)
