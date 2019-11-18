class Laptop:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self): # Display Value - View
        return self.__name

    def set_name(self, name):  # Takes the Variable name - Update
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


lap = Laptop("HP", 150000)
ans = lap.get_name(), lap.get_price()
print(ans)