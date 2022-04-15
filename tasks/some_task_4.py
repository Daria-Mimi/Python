# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in a:
#     if elem < 5:
#         print(elem)

# print([elem for elem in a if elem < 5])

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = [elem for elem in a if elem in b]
# result = list(set(a) & set(b))
# print(result)


# def decorator(func):
#     def some_func():
#         print("Реклама")
#         func()
#     return some_func
#
# @decorator
# def some_func_2():
#     print("Hello world!")
# #
# #
# # res = decorator(some_func_2)
# print(some_func_2())


# def decorator(func):
#     def original_func():
#         print("Some text")
#         func()
#     return original_func
#
# @decorator
# def alone_function():
#     print("Hello world!")


# function_decorated = decorator(alone_function)
# function_decorated()
# alone_function()

# def decorator(func):
#     def some_func():
#         print("Hello world!")
#         return func()
#     return some_func
#
# @decorator
# def hello():
#     return "Реклама!"
#
#
# c = hello()
# print(c)
#
#
# # параметризованный декоратор
# def some_dec(*args, **kwargs):
#     def decorator(func):
#         def some_func():
#             print("Hello world!")
#             return func()
#         return some_func
#     return decorator
#
# @decorator()
# def hello():
#     return "Реклама!"
#
#
# c = hello()
# print(c)


# def search(l):
#     for i in range(0, 101):
#         if l[i] == l1[i]:
#             return l[i]

def outer_1(*dargs, **dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            print(*dargs, **dkwargs)
            return func(*args, **kwargs)
        return inner
    return outer

def div(a, b):
    return a * b

simple = outer_1("Hello")(div)(2, 3)
print(simple)