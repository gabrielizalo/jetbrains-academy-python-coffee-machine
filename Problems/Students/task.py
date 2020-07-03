class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.calculate_id()

    def calculate_id(self):
        return self.name[0] + self.last_name + self.birth_year


student_name = input()
student_last_name = input()
student_birth_year = input()
my_student = Student(student_name, student_last_name, student_birth_year)
print(my_student.id)
