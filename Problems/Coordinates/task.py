pos_x = float(input())
pos_y = float(input())

if pos_x >= 0 and pos_y >= 0:
    print('I')
elif pos_x < 0 <= pos_y:
    print('II')
elif pos_x < 0 and pos_y < 0:
    print('III')
else:
    print('IV')
