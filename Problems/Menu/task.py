pizza = 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy'
salad = 'Caesar salad, Green salad, Tuna salad, Fruit salad'
soup = 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'

user_order = input()
if user_order == 'pizza':
    print(pizza)
elif user_order == 'salad':
    print(salad)
elif user_order == 'soup':
    print(soup)
else:
    print("Sorry, we don't have it in the menu")
