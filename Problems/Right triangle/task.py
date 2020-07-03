class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.is_right = self.validate_right()
        self.area = self.calculate_area()

    def calculate_area(self):
        return 0.5 * self.a * self.b

    def validate_right(self):
        if pow(self.c, 2) == pow(self.a, 2) + pow(self.b, 2):
            return True
        else:
            return False


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
my_right = RightTriangle(input_c, input_a, input_b)
if my_right.is_right:
    print(f'{my_right.area:.1f}')
else:
    print('Not right')
