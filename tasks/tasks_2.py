from datetime import datetime

#  обычный декоратор

# def deco(func):
#     def outer():
#         print("Hello")
#         func()
#         return func
#     return outer
#
# @deco
# def hel():
#     return "blablabla"
#
# bla = hel()
# print(bla)



# декоратор

# def deco(func):
#     def outer(*args, **kwargs):
#         print("blablabla")
#         func(*args, **kwargs)
#         # return func
#     return outer
#
# @deco
# def some_func(a, b):
#     return a + b
#
# # c = some_func(5, 2)
# some_func(5, 2)


#  параметризованный декоратор

# def deco(smht):
#     def outer(func):
#         def inner(*args, **kwargs):
#             start = datetime.now()
#             func(*args, **kwargs)
#             print(datetime.now() - start)
#             print(smht)
#             return func
#         return inner
#     return outer
#
#
# @deco("hello")
# def simple(a, b):
#     print("some work")
#     return a * b
#
# simple(2, 4)


# ретрай декоратор

# def deco(count):
#     def outer(func):
#         def inner(*args, **kwargs):
#             cnt = 0
#             while cnt <= 10:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"Error {err}, попыток осталось {count - cnt}")
#                 cnt += 1
#         return inner
#     return outer
#
#
# @deco(10)
# def simple(a, b):
#     return a / b
#
# print(simple(2, 4))


def retryer(count):
    def deco(func):
        def inner(*args, **kwargs):
            cnt = 0
            while cnt <= count:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"Error {err}, попыток осталось {count - cnt}")
                cnt += 1
        return inner
    return deco



@retryer(5)
def simple(a, b):
    return a / b

print(simple(1, 0))