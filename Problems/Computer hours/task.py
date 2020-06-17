# Make sure your output matches the assignment *exactly*
hours_computer = int(input())
if hours_computer < 2:
    print('That seems reasonable')
elif hours_computer < 4:
    print('Do you have time for anything else?')
else:
    print('You need to get outside more!')
