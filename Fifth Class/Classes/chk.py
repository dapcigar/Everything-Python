class Person:
    def __init__(self, name, age, sex, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary


    def check_user(self):
        if self.sex == "Male":
            result = self.salary * 5
            return result

        else:
            result = self.salary * 7
        return result



chk = Person("Ola", 23, "Male", 10000)

res = chk.check_user()
print(res)