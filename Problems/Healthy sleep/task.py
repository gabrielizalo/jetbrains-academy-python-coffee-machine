AA = int(input())
BB = int(input())
HH = int(input())

if HH < AA:
    print('Deficiency')
else:
    if HH > BB:
        print('Excess')
    else:
        print('Normal')
