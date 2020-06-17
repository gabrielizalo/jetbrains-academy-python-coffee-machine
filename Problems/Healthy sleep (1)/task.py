hours_a = int(input())
hours_b = int(input())
hours_h = int(input())

if hours_h < hours_a:
    print('Deficiency')
elif hours_h > hours_b:
    print('Excess')
else:
    print('Normal')
