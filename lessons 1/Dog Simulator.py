class Dog:
    def __init__(self, name, color, sex):
        self.color = color
        self.name = name
        self.sex = sex

    def bark(self, count):
        for i in range(count):
            print("Woof!")

    def eat(self):
        print("Am! Mmmmm!")


myDog = Dog('Umka', 'Brown', 'Male')
secondDog = Dog('Jim', 'Pale', 'Male')

print(myDog.name)
print(myDog.color)
print(myDog.sex)
myDog.bark(2)
myDog.eat()

print("")

print(secondDog.name)
print(secondDog.color)
print(secondDog.sex)
myDog.bark(1)
