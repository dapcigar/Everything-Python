
try:
    file_handler = open("python.txt","r")
    # file_handler.write("Lets party")
    res = file_handler.read()
    print(res)

except FileNotFoundError:
    print("Ooopps File not Found!!")

finally:
    file_handler.close()



