# Ini
machine_money = 550
machine_water = 400
machine_milk = 540
machine_beans = 120
machine_cups = 9


# Functions
def print_machine_state():
    print("The coffee machine has:")
    print(machine_water, "of water")
    print(machine_milk, "of milk")
    print(machine_beans, "of coffee beans")
    print(machine_cups, "of disposable cups")
    print(machine_money, "of money")
    print()


def action_buy():
    global machine_money
    global machine_water
    global machine_milk
    global machine_beans
    global machine_cups

    machine_cups = machine_cups - 1
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = int(input())

    if coffee_type == 1:
        machine_money = machine_money + 4
        machine_water = machine_water - 250
        machine_beans = machine_beans - 16
    elif coffee_type == 2:
        machine_money = machine_money + 7
        machine_water = machine_water - 350
        machine_milk = machine_milk - 75
        machine_beans = machine_beans - 20
    elif coffee_type == 3:
        machine_money = machine_money + 6
        machine_water = machine_water - 200
        machine_milk = machine_milk - 100
        machine_beans = machine_beans - 12


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
print_machine_state()

print("Write action (buy, fill, take):")
action = input()
if action == "buy":
    action_buy()
elif action == "fill":
    action_fill()
elif action == "take":
    action_take()

print_machine_state()
