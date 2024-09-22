from symtable import Class
from traceback import format_exc

import requests

class Human:
    pass


rq = requests

jack = Human
print("================================")
#__name__
print(requests.__name__)
print(rq.__name__)
print(jack.__name__)
print(Human.__name__)
print(__name__)
#type()
print(type(rq))
print(type(Human))
#dir()

list_cars = ["Tesla", "Toyota", "BMW"]
print("================================")
for method in dir(list_cars):
    #print(method, getattr(list_cars, method))
    print(method)
print("================================")
for method in dir():
    print(method)
    print("================================")

data = "string"


print(hasattr(data, "reverse"))
print(hasattr(data, "replace"))

print("================================")

print(getattr(data, "startswith"))
print(getattr(data, "startswith", None))
print(getattr(data, "reverse", None))

print("================================")

print(callable(data))
print(callable(list_cars))


class First:
    pass

class Second:
    pass


print(issubclass(First, Second))
print(issubclass(Second, First))


first = First()
second = Second()

print(isinstance(first, Second))
print(isinstance(second, First))

print("============INSPECT===============")

import inspect

print(inspect.isclass(requests))
print(inspect.ismodule(requests))
print(inspect.isfunction(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
print("==================")
class Human:
    def __init__(self, age, name="Jack"):
        self.age = age
        self.name = name

s_human = inspect.signature(Human)
for param in s_human.parameters.values():
    print(param.name)
    print(param.kind)


print("=======SYS=======")

import sys

print(sys.version)
print(sys.executable)
print(sys.platform)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)