# Remove duplicate from the list [4,6,3,2,4]

value = [4, 6, 3, 2, 4]
print(f"The original list is : {value}")

res = []
# first For Loop to check all the Value
for i in value:
    # Check if the value is not added to the new list
    if i not in res:
        res.append(i)
        # printing list after removal
print(f"The Unique list is : {res}")
