# class A:
#     def public(self):
#         print("публичный метод")
#
#     def _protected(self):
#         print("защищенный метод")
#
#     def __private(self):
#         print("приватный метод")


# class A:
#     def __init__(self, name):
#         self.name = name
#
# class B(A):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"My name is {self.name}, I'm {self.age} years old.")
#
#     def voice(self):
#         print("meow meow")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"My name is {self.name}, I'm {self.age} years old.")
#
#     def voice(self):
#         print("bork bork")
#
# kitty = Cat("Bars", 5)
# dog = Dog("Bob", 6)
#
# for animal in (kitty, dog):
#     animal.voice()
#     animal.info()
#     animal.voice()


# class A:
#     def __enter__(self):
#         print('работа метода enter')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('работа метода exit')
#
# obj = A()
#
# with obj:
#     print('работа внутри контекста')
#
# print('работа после всего')


# def deco(smht):
#     def outer(func):
#         def inner(*args, **kwargs):
#             func(*args, **kwargs)
#             print(smht)
#             return func
#         return inner
#     return outer
#
# @deco("Hello")
# def simple(a, b):
#     return a * b


# def retry(count):
#     def deco(func):
#         def inner(*args, **kwargs):
#             cnt = 0
#             while cnt <= count:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"Ошибка {err}, попток осталось {count - cnt}")
#                 cnt += 1
#         return inner
#     return deco
#
#
# @retry(5)
# def simple_2(a, b):
#     return a / b
#
# sim = simple_2(3, 0)


# def gen(num):
#     cnt = 0
#     while cnt < num:
#         cnt += 1
#         yield f"Яблоко № {cnt}"
#
#
# gen_o = gen(5)
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))


# col = [1, 2, 3, 4, 5, 6, 7]
# for el in col:
#     print(el)

# def deco(param):
#     def outer(func):
#         def inner(*args, **kwargs):
#             func(*args, **kwargs)
#             print(param)
#             return func
#         return inner
#     return outer
#
# @deco("hello")
# def simple(a, b):
#     return a * b
#
# simple(2, 4)


# def deco(count):
#     def outer(func):
#         def inner(*args, **kwargs):
#             cnt = 0
#             while cnt < count:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"Ошибка {err}, попыток осталось {count - cnt}")
#                 cnt += 1
#         return inner
#     return outer
#
# @deco(5)
# def simple(a, b):
#     return a / b
#
#
# simple(3, 0)

# def gen(num):
#     cnt = 0
#     while cnt < num:
#         cnt += 1
#         yield f"apple № {cnt}"

# gen_o = gen(5)
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я кошка, меня зовут {self.name}, мне {self.age}")
#
#     def voice(self):
#         print("Мяу мяу мяу")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я собака, меня зовут {self.name}, мне {self.age}")
#
#     def voice(self):
#         print("Гав гав гав")
#
# kitty = Cat("Murka", 5)
# pappy = Dog("Miki", 3)
#
# for animal in (kitty, pappy):
#     animal.voice()
#     animal.info()
#     animal.voice()


# class Context:
#     def __enter__(self):
#         print("Работает метод enter")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Работает метод exit")
#
# obj = Context()
#
# with obj:
#     print("Работа внутри контекста")
#
# print("Работа после всего")