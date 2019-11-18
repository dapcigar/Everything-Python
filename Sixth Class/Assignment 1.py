class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


class CustomerCalulate(Customer):
    def __init__(self, yrs, amt, price, name, phone, email):
        super().__init__(name, phone, email)
        self.__yrs = yrs
        self.__amt = amt
        self.__price = price

    def get_yrs(self):
        return self.__yrs

    def set_yrs(self, yrs):
        self.__yrs = yrs

    def get_amt(self):
        return self.__amt

    def set_amt(self, amt):
        self.__amt = amt

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def Calculate_Discount(self):
        if self.get_yrs() > 20 and self.get_amt() >= 1000000:
            discounted_amount = self.get_price() - (self.get_price() * 0.1)
            print(
                f" Hello, {self.get_name()}, Thank you for being our loyal Customer,\n You get 10% discount for being a loyal customer for over {self.get_yrs()}.\nThe Original price is {self.get_price()},  The Total amount to "
                f"pay after discount is {discounted_amount} ")

        else:
            print(f" Hello {self.get_name()},\n We only give discount to customers over 10yrs and over 1000000 transactions but you did not meet the requirement\n. You have only been with us for {self.get_yrs()} and transacted only {self.get_amt()} \n The total Amount to pay is {self.get_price()}")


cus = CustomerCalulate(10, 500000, 54000, "Oladeinde", "0904493883", "Olabola@yahoo.com")
cus.Calculate_Discount()
