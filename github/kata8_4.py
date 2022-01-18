"""
https://www.codewars.com/kata/57eae65a4321032ce000002d/

"""
# 1
# el = []
# def fake_bin(x):
#     for res in x:
#         if int(res) < 5:
#             res = 0
#             el.append(res)
#         else:
#             res = 1
#             el.append(res)
#     return print(repr(''.join(str(e) for e in el)))
#
# fake_bin("45385593107843568")


# 2
# user = int(input('Введите число: '))
# count = 0
# while user > 0:
#     if user % 10:
#         user = user // 10
#     count += 1
# print(count)

# 3
# num = int(input('число: '))
# count = 0
# while num > 0:
#     res = num % 10
#     num //= 10
#     count *= 10
#     count += res
#     print(count)

# num = input('число: ')
# for res in reversed(num):
#     print(res)

# 4
# num = input('число: ')
# for res in num:
#     print(res)

# 5
# user = int(input('число: '))
# count = 0
# while user > 0:
#     if user % 2 == 0:
#         count += 1
#     user //= 10
# print(count)

# 6
# user = input('число: ')
# count = 0
# for res in user:
#     if res == "1":
#         count += 1
#     else:
#         continue
# print(count)

# def cat_voice():
#     print('Meow!')
#
# cat_voice()
# cat_voice()
#
# def dog_voice():
#     print('Woof!')
#
# dog_voice()
# dog_voice()

# def get_voice(text):
#     return print(text + "!")
#
# get_voice("Hello my friend")

# # Without List Comprehension
# some_list = []
# def func(a, b):
#     res = range(a, b + 1)
#     for el in res:
#         if el % 2:
#             some_list.append(el)
#     return print(some_list)
# 
# func(1, 11)
#
# # With List Comprehension
# def func_2(a, b):
#     some_list = list(range(a, b + 1))
#     number_list = [number for number in some_list if number % 2]
#     return print(number_list)
#
# func_2(1, 10)