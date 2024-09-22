class JackNameError(Exception):
    def __init__(self, name):
        self.name = name
        print(name)


    def __str__(self):
        return f'{self.name}is an invalid name'





def check_name():
    name = input("Enter your name: ")
    if name.lower() == "jack":
        raise NameError("Jack is not very good!")
    else:
        print("Is good name")




check_name()