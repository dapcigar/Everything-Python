# num_1 = input("Enter The First number: ")
# num_2 = input("Enter The Second Number: ")
#
# total = int(num_1)  + int(num_2)
#
# fh = open("number.txt","w")
# fh.write(f" you answer is {total}")
#
# fh.close()

# both = int(input("Enter the amount of Both girls have"))
# gia=(input("Enter the amount of Apples gia has"))
#
# total = both - gia
#
# difference  = both - gia
#
# print (total)
# print (difference)

import fileinput
import sys

for line in fileinput.input():
    sys.stdout.write(line)