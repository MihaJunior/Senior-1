from itertools import count

list_car = ["one","two","three","four","five"]


iterator = iter(list_car)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("================================")

for car in iterator:
    print(car)

#print(next(iterator))


class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

counter = Counter(5)

#for counter in counter:
#   print(counter)

print(counter.__next__())
print(counter.__iter__())
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#============== generator ===============

def num_to_degrees(number, max_degree):
    i=0
    for deg in range(max_degree):
        yield number**i
        i+=1

def num_to_degrees(number, max_degree):
    i=0
    while True:
        result = number**i
        yield result
        if result > number ** 5:
            return
        i+=1

res = num_to_degrees(5, 4)
print(res)

for num in res:
    print(num)

print("=======")


print("Замикання функції")

class Helper:

    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"Self = {self.work}, no self = {work}"

helper = Helper("calsswork")
print(helper("homework"))

def checker(function):

    def checker(*args, **kwargs):
        try:
            res = function(*args, **kwargs)
        except Exception as e:
            print(e)
        else:
            print(f"No problems. Result: {res}")

    return checker
@checker
def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate("5+7+12")

