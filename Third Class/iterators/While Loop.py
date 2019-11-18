import random as ayo  # Alias a method using the as keyword.

from random import randint # using the exact Method

num = 1
while num <= 10:

   # print(num)

    num = num + 1

    num2 = randint(1, 3)

    print(num2 + num)

# num2 = ayo.randint(1, 5) # using the method alias to call the method

# num2 = randint(1, 5) # If you decide to get the direct method.
#
# print(num2)
