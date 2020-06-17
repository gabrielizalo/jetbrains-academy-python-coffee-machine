student_score = int(input())
maximum_score = int(input())

multiplier = maximum_score / 100
if student_score < 60 * multiplier:
    print('F')
elif student_score < 70 * multiplier:
    print('D')
elif student_score < 80 * multiplier:
    print('C')
elif student_score < 90 * multiplier:
    print('B')
else:
    print('A')
