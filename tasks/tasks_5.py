"""
https://www.codewars.com/kata/5672a98bdbdd995fad00000f
https://www.codewars.com/kata/56cd44e1aa4ac7879200010b

"""

# 1
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"
#
# print(rps('rock', 'scissors'))
# print(rps('scissors', 'rock'))
# print(rps('paper', 'rock'))
# print(rps('rock', 'rock'))
#
#
# def deco(param):
#     def inner(func):
#         def outer(*args, **kwargs):
#             print(param)
#             return func(*args, **kwargs)
#         return outer
#     return inner


# 2
# def is_uppercase(inp):
#     return inp.isupper()
#
# print(is_uppercase("c"))
# print(is_uppercase("C"))
# print(is_uppercase("hello I AM DONALD"))
# print(is_uppercase("HELLO I AM DONALD"))
# print(is_uppercase("$%&"))


# def gen(num):
#     cnt = 0
#     while cnt < num:
#         cnt += 1
#         yield f"яблоко № {cnt}"
#
# gen_o = gen(7)
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))
# print(next(gen_o))



# def deco(param):
#     def inner(func):
#         def outer(*args, **kwargs):
#             print(param)
#             return func(*args, **kwargs)
#         return outer
#     return inner
#
#
# @deco("hello")
# def simple(a, b):
#     return a * b
#
# @deco("world")
# def simple_2(a, b):
#     return a + b
#
# print(simple(2, 5))
# print(simple_2(2, 5))

# def deco(count):
#     def inner(func):
#         def outer(*args, **kwargs):
#             cnt = 0
#             while cnt < count:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f'Ошибка {err}, попыток осталось {count - cnt}')
#                 cnt += 1
#         return outer
#     return inner
#
#
# @deco(5)
# def simple_2(a, b):
#     return a / b
#
# # print(simple_2(4, 0))
# print(simple_2(4, 2))

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

# user = "3"
# # print(f"{user} + {user + user} + {user + user + user} = {int(user) + int(user + user) + int(user + user + user)}")
# def func(user: str):
#     print(f"{user} + {user + user} + {user + user + user}")
#     return int(user) + int(user + user) + int(user + user + user)
#
# res = func('3')
# print(res)
