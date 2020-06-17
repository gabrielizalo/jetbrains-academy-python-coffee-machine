london_hour = 10.5
offset = float(input())
user_hour = london_hour + offset
if user_hour < 0:
    print('Monday')
elif user_hour >= 24:
    print('Wednesday')
else:
    print('Tuesday')
