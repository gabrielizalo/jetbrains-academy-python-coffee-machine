# Ini
machine_money = 550
machine_water = 400
machine_milk = 540
machine_beans = 120
machine_cups = 9


# Functions
def action_remaining():
    print("The coffee machine has:")
    print(machine_water, "of water")
    print(machine_milk, "of milk")
    print(machine_beans, "of coffee beans")
    print(machine_cups, "of disposable cups")
    print("$", machine_money, "of money")
    print()


def action_buy():
    global machine_money
    global machine_water
    global machine_milk
    global machine_beans
    global machine_cups

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_type = input()

    if coffee_type != "back":
        if coffee_type == "1":
            if machine_water >= 250 and machine_beans >= 16:
                print("I have enough resources, making you a espresso coffee!")
                machine_money = machine_money + 4
                machine_water = machine_water - 250
                machine_beans = machine_beans - 16
                machine_cups = machine_cups - 1
            else:
                print("I don't have enough resources to make you a espresso coffee!")
        elif coffee_type == "2":
            if machine_water >= 350 and machine_milk >= 75 and machine_beans >= 20:
                print("I have enough resources, making you a latte coffee!")
                machine_money = machine_money + 7
                machine_water = machine_water - 350
                machine_milk = machine_milk - 75
                machine_beans = machine_beans - 20
                machine_cups = machine_cups - 1
            else:
                print("I don't have enough resources to make you a latte coffee!")
        elif coffee_type == "3":
            if machine_water >= 200 and machine_milk >= 100 and machine_beans >= 12:
                print("I have enough resources, making you a cappuccino coffee!")
                machine_money = machine_money + 6
                machine_water = machine_water - 200
                machine_milk = machine_milk - 100
                machine_beans = machine_beans - 12
                machine_cups = machine_cups - 1
            else:
                print("I don't have enough resources to make you a cappuccino coffee!")


def action_fill():
    global machine_money
    global machine_water
    global machine_milk
    global machine_beans
    global machine_cups
    print("Write how many ml of water do you want to add:")
    user_water = int(input())
    print("Write how many ml of milk do you want to add:")
    user_milk = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    user_beans = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    user_cups = int(input())
    machine_water = machine_water + user_water
    machine_milk = machine_milk + user_milk
    machine_beans = machine_beans + user_beans
    machine_cups = machine_cups + user_cups


def action_take():
    global machine_money
    print("I gave you $", machine_money)
    machine_money = 0


# Main program
print("Write action (buy, fill, take, remaining, exit):")
action = input()

while action != "exit":
    if action == "buy":
        action_buy()
    elif action == "fill":
        action_fill()
    elif action == "take":
        action_take()
    elif action == "remaining":
        action_remaining()

    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
