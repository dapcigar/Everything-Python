class Person:  # Create the Class
    def __init__(self, name, age, gender):
        # Set your Variables
        self.name = name
        self.age = age
        self.gender = gender

    # Write a Method to print the result.
    def get_info(self):
        return f"my name is {self.name}, i'm {self.age} years and i am a {self.gender} "

    def __str__(self):
        return f"my name is {self.name}, i am a {self.gender}"


p1 = Person("Ola", 27, "Male")  # p1 is the instance of the Class Person
person_info = p1.get_info()
print(person_info)

# Instantiate STR
my_info = p1.__str__()
print(my_info)

