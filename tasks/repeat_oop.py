# class Phone:
#     number = "111-11-11"
#     def print_number(self):
#         print("Phone number is: ", self.number)

# my_phone = Phone()
# my_phone.print_number()


#  Инкапсуляция
# class B:
#     def __private(self):
#         print("Это приватный метод!")
#
# b = B()
# b.__private()

class A:
    def public(self):
        print("Это публичный метод!")

    def _protected(self):
        print("Это защищённый метод!")

    def __private(self):
        print("Это приватный метод!")

a = A()
pub = a.public()
prot = a._protected()
priv = a.__private()