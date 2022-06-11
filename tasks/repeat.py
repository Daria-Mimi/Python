from datetime import datetime

# class A:
#     def public(self):
#         print("public method")
#
#     def _protected(self):
#         print("protected method")
#
#     def __private(self):
#         print("private method")
#
# class A:
#     def __init__(self, date):
#         self.date = date
#
#
# class B(A):
#     def __init(self, date, city):
#         super().__init__(date)
#         self.city = city


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Me name is {self.name}. I'm {self.age} years old")
#
#     def voice(self):
#         print("Meow meow")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Me name is {self.name}. I'm {self.age} years old")
#
#     def voice(self):
#         print("Bark bark")
#
# cat = Cat("Kitty", 3)
# dog = Dog("Bob", 5)
#
# for animal in (cat, dog):
#     animal.voice()
#     animal.info()
#     animal.voice()

# def deco(smth):
#     def outer(func):
#         def inner(*args, **kwargs):
#             start = datetime.now()
#             func(*args, **kwargs)
#             print(smth)
#             print(f"Time {datetime.now() - start}")
#             return func
#         return inner
#     return outer
#
# @deco("hello")
# def simple(a, b):
#     return a * b
#
# simple(2, 4)

# def retry(count):
#     def deco(func):
#         def inner(*args, **kwargs):
#             cnt = 0
#             while cnt <= count:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"Ошибка {err}, попыток осталось {count - cnt}")
#                 cnt += 1
#         return inner
#     return deco
#
# @retry(5)
# def simple(a, b):
#     return a / b
#
# print(simple(4, 3))

# def polindrom(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
# print(polindrom("topt"))

# def gen(num):
#     cnt = 0
#     while cnt < num:
#         cnt += 1
#         yield f"яблоко № {cnt}"
#
# gen_o = gen(7)
# print(next(gen_o))


# class Context:
#     def __enter__(self):
#         print("запускаем метод enter")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("запусаем метод exit")
#
# obj = Context()
#
# with obj:
#     print("какая-то работа")
#
# print("работа после всего")


