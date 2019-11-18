

person_name='kola'
person_age= 32
person_gender='female'

#Using F-String
# print(f"my name is {person_name}  and my age is {person_age} and my gender is  {person_gender}")

#Using Format String
#print("my name is {0}  and my age is {1} and my gender is  {2}".format(person_name, person_age, person_gender))

my_type = type(person_age)
print(my_type)

my_loc = id(person_age)
print(my_loc)