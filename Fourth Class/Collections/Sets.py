my_fruits = {"Apples", "Oranges", "Banana", "Oranges","Kiwi", "Cherry"}
my_fruist2 = {"Carrots", "Cucumber", "Strawberries", "Grapes", "Banana", "Water Melon"}

print(my_fruits)

# res = "Oranges" not in my_fruits
# print(res)

res = my_fruits.intersection(my_fruist2)
res2= my_fruits.union(my_fruist2)
res3 = my_fruits.difference(my_fruist2)

my_fruits.add("Spring onions")
my_fruist2.remove("Carrots")

result = set("Hanna")

print(result)

print(res)
print(res2)
print(res3)
print(my_fruits)
print(my_fruist2)

for fr in my_fruist2:
    print(fr)