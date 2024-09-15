class Student:
    count = 0
    def __init__(self, name, age = 10, height = 150):
        self.name = name
        self.age = age
        self.height = height
        Student.count += 1


    def show(self):
        print("=========================")
        print("Ім'я = ", self.name)
        print("Вік = ", self.age)
        print("Зріст = ", self.height)

    def __str__(self):
        return "Hello, my name is " + self.name + "!"



jack_student = Student(name="Jack", age=18, height=160)
kirril_student = Student(name="Kirill", age=20, height=154)
bob_student = Student("Bob")

jack_student.show()
kirril_student.show()
bob_student.show()

print(jack_student)
print(kirril_student)
print(bob_student)


