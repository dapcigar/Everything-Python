# using List and For Loop to Print out F

for row in range(10):
    for col in range(12):
        if (col == 0 or col == 1) or ((row == 0 or row == 1 or row == 4 or row == 5 ) and col > 0):
            print("*", end="")
        else:
            print(end="")
    print()
