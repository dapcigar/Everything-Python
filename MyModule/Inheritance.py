class Employee:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# Never use Private with Inheritance


class Ftemployee(Employee):
    def __init__(self, salary, name, age, gender):
        super().__init__(name, age, gender)
        self.__salary = salary

    def get_name(self):  # Display Value - View
        return self.name

    def set_name(self, name):  # Takes the Variable name - Update
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_all_info(self):
        print(
            f" Name is {self.get_name()}, Age = {self.get_age()}, Gender = {self.get_gender()}, Salary = {self.get_salary()}")


emp = Ftemployee(3000, "Ola", 12, "Male")
emp.get_all_info()
