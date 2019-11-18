# Create a Class
class Laptop:
    # This is a Constructor
    def __init__(self, name, price):
        self.__name = name
        self.price = price

    def __add__(self, other):
       self.price + other.price



    def __sub__(self, other):
       res =  self.price - other
       return res

    def __lt__(self, other):
      res = self.price < other
      return res

    def __gt__(self, other):
        self.price > other


Lap = Laptop("Hp", 345000)
Lap2 = Laptop("Dell", 5787773)

res = Lap.__add__(Lap2)
print(res)

