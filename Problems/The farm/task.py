money = int(input())

# Sheep: 6769
if money >= 6769:
    print(money // 6769, 'sheep')

# Cow: 3848
elif money > 3848 * 2:
    print(money // 3848, 'cows')
elif money >= 3848:
    print('1 cow')

# Pig: 1296
elif money >= 1296 * 2:
    print(money // 1296, 'pigs')
elif money >= 1296:
    print('1 pig')

# Goat: 678
elif money >= 678 * 2:
    print(money // 678, 'goats')
elif money >= 678:
    print('1 goat')

# Chicken: 23
elif money >= 23 * 2:
    print(money // 23, 'chickens')
elif money >= 23:
    print('1 chicken')

# None
else:
    print('None')
