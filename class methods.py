class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        average = 0
        for student in self.students:
            average += student.get_grade()
        return average/len(self.students)

s1 = student('nick', 18, 90)
s2 = student('mike', 18, 80)
s3 = student('issac', 18, 70)

course = Course('math', 2)

course.add_student(s1)
course.add_student(s3)

print(course.students)  # we get a list of objects as output
print(course.get_avg_grade())
print(course.students[0].get_grade())
print(course.add_student(s2))  # this  prints a 'False' because the max_students we specified are 2

# class attributes
class Person:
    num_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count_objects()

    def about(self):
        return f'name is {self.name} and age is {self.age}'

    # class methods
    @classmethod
    def count_objects(cls):
        Person.num_people += 1

p1 = Person('tim', 20)
p2 = Person('mike', 23)
p3 = Person('cam', 25)
print(Person.num_people)  # gives number of objects created



# static methods