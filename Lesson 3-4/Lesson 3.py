class Human:
    def __init__(self, name = "Humam"):
        self.name = name

class Automobile:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passenger_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"No passengers found in {self.brand}")

misha = Human("Misha")
maxim = Human("Max")
jack = Human("Jack")

car = Automobile("Dodhe Challenger")
car.add_passenger(misha, maxim, jack)
#
# car = Automobile("Dodge Challenger")
# car.add_passenger(misha)
# car.add_passenger(maxim)
# car.add_passenger(jack)
# car.print_passenger_names()
car.print_passenger_names()
