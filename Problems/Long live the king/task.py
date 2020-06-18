coordinator_a = int(input())
coordinator_b = int(input())

if 1 < coordinator_a < 8 and 1 < coordinator_b < 8:
    print('8')
elif (coordinator_a == 1 and coordinator_b == 1) or (coordinator_a == 8 and coordinator_b == 8):
    print('3')
elif (coordinator_a == 1 and coordinator_b == 8) or (coordinator_a == 8 and coordinator_b == 1):
    print('3')
else:
    print('5')
