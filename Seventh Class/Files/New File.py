


# fh = open("MyFile.txt", "r")
# print("Printing all Lines")
# for lines in fh:
#     print(lines)

# fh = open("My_New_File.txt", "w")
# fh.write(
#     "The TENDER must give the full legal name and registered office of TENDERER and, if applicable, \nthe jurisdiction in which it is registered or incorporated. The TENDER must be signed by its duly authorized representative. If requested by COMPANY, TENDERER agrees to use COMPANY’s designated on-line tool to sign with a digital signature, except where prohibited by APPLICABLE LAW. If signed digitally, TENDERER agrees to waive any right to dispute the genuineness of the signature, \n or the admissibility of its TENDER or COMPANY’s ITT where such challenge is based on the absence of a physical signature.")
#
# fh.close()


with open("My_New_File.txt", "r") as fh:
      for line in fh:
         print(line)
