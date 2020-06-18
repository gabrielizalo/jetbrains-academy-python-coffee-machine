print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
no_cups = int(input())

list_cups = [water // 200, milk // 50, beans // 15]
min_cups = min(list_cups)
print(min_cups)

if no_cups == min_cups:
    print('Yes, I can make that amount of coffee')
elif no_cups > min_cups:
    print('No, I can make only', min_cups, 'cups of coffee')
else:
    print('Yes, I can make that amount of coffee (and even', min_cups - no_cups, 'more than that)')
