# Print a Pyramid

size = 10
m = (2 * size) - 2
# outer loop to handle number of rows
for row in range(0, size):
    # inner loop to handle number spaces
    for col in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    # inner loop to handle number of column
    for col in range(0, row + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")