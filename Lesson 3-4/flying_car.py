class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("Я їду")


class Plane:
    def __init__(self, type):
        self.type = type

    def fly(self):
        print("Я лечу!")


class FlyingCar(Car, Plane):
    def __init__(self, model, type):
        Car.__init__(self, model)
        Plane.__init__(self, type)

    def start_flying(self):
        print(f"Моя машина {self.model} летить як {self.type}!")


my_flying_car = FlyingCar(model="Dodge Challenger", type="Boeing 737")
my_flying_car.drive()
my_flying_car.start_flying()
my_flying_car.fly()