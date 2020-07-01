income = int(input())

percent = 0
if 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
elif income >= 132407:
    percent = 28

calculated_tax = income * percent / 100
calculated_tax_rounded = int(round(calculated_tax))
print(f'The tax for {income} is {percent}%. That is {calculated_tax_rounded} dollars!')
