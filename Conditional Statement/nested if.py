
cus_current_trans =0
cus_name = input("Enter your name :")
cus_year = input("Enter years of Service : ")
cus_current_trans= input("Enter your Current Transaction : ")

cheking = 1000000
num =int(cheking)

cus_after_dis_trans = 0
year= int(cus_year)
convert = float(cus_current_trans)




if(year>=10):
    if(convert >=num):
        cus_after_dis_trans =convert - (float(convert * 0.1))
        print(f"Congratulations {cus_name}, you get 10% discount for transacting over {cus_year} with us. the total discount is {cus_after_dis_trans} ")
    else:
        print(f"Sorry {cus_name}, you have only been here for {cus_year} don't get a discount this time")
else: print(f"{cus_name}, you are not qualified for any discount because the requirement is 10 years and above ")