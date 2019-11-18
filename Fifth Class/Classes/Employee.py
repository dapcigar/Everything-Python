class Employee:
    def __init__(self, name, age, gender, salary, location):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.location = location

    def calculate_sal(self):
        tax = (self.salary * 0.1)
        sal_after = self.salary - tax

        return f"Name : {self.name} \n " \
               f"Age: {self.age} \n" \
               f"Salary: {self.salary} \n" \
               f"Tax: {tax} \n" \
               f"Net Income: {sal_after}\n" \
               f"Gender : {self.gender}\n" \
               f"Location : {self.location} "

    def __str__(self):
        tax = (self.salary * 0.1)
        sal_after = self.salary - tax

        return f"Name : {self.name} \n " \
               f"Age: {self.age} \n" \
               f"Salary: {self.salary} \n" \
               f"Tax: {tax} \n" \
               f"Net Income: {sal_after}\n" \
               f"Gender : {self.gender}\n" \
               f"Location : {self.location} "


emp = Employee("Mike", 22, "Male", 30000, "Lagos")
show_emp = emp.calculate_sal()
chk_emp = emp.__str__()
print(chk_emp)
