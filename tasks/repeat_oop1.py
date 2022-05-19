# Наследование
# class Parent():
#     def who(self):
#         print("I am a parent")
#
# class Child(Parent):
#     def play(self):
#         print("I am playing")
#
# parent = Parent()
# parent.who()
# child = Child()


# Переопределение метода
# class Parent():
#     def who(self):
#         print("I am a parent")
#
# class Child(Parent):
#     def play(self):
#         print("I am playing")
#
#     def who(self):
#         print("I am a child")
#
#
# parent = Parent()
# parent.who()
# child = Child()
# child.who()

# Множественное наследование
# class Account():
#     def __init__(self, name, number):
#         self.Name = name
#         self.Number = number
#
#     def display(self):
#         print(f"Account # : {self.Number}\nAccount Name : {self.Name}")
#
#
# class Customer():
#     def __init__(self, name, number):
#         self.Name = name
#         self.Number = number
#
#     def display(self):
#         print(f"Customer # : {self.Number}\nCustomer Name : {self.Name}")
#
#
# class Orders(Account, Customer):
#     def __init__(self, acctnumber, acctname, custnumber, custname, ordnumber, ordnamename, product, qty):
#         self.OrdNumber = ordnumber
#         self.Product = product
#         self.Qty = qty
#         self.OrdName = ordnamename
#         self.acct = Account(acctname, acctnumber)
#         self.cust = Customer(custname, custnumber)
#
#     def display(self):
#         print("Order Information")
#         self.acct.display()
#         self.cust.display()
#         print(f"Order # : {self.OrdNumber}\nOrder Name : {self.OrdName}\nProduct : {self.Product}\nQuantiy : {self.Qty}")


# acct = Account("AB Enterprise", 12345)
# acct.display()
# print("")
# cust = Customer("John Smith", 45678)
# cust.display()
# print("")
# order = Orders(12345, "AB Enterprise", 45678, "John Smith", 1, "Order 1", "Widget", 5, )
# order.display()

#  использование super()
class Parent():
    def __init__(self, name):
        self.name = name

    def who(self):
        print("I am a parent")

class Child(Parent):
    def __init__(self, name, do):
        super().__init__(name)
        self.do = do

    def play(self):
        print("I am playing")

    def who(self):
        print("I am a child")

parent = Parent("Alla")
child = Child("Alla", "eat")
print(child.do)