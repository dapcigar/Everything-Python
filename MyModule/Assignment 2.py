
class Car:
    def type(self):
        print("Sedan ")
    def wheels(self):
        print("Two Wheel Drive")

class Suv:
    def type(self):
        print("Sport Ultility Vehicle")
    def wheels(self):
        print("Four Wheel Drive")

class Tricycle:
    def type(self):
        print("It's a Tricycle")
    def wheels(self):
        print("There tyres")


class Vehicle:
    def poly(inst):
        inst.type()
        inst.wheels()


keke = Tricycle()
jeep = Suv()

Vehicle.poly(jeep)


