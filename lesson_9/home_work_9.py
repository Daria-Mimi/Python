# Задачи с codewars

# https://www.codewars.com/kata/5966e33c4e686b508700002d

# Варинат решения 1
# def sum_str(a, b):
#     if a != "":
#         a = int(a)
#     else:
#         a = 0
#     if b != "":
#         b = int(b)
#     else:
#         b = 0
#     res = str(a + b)
#     return res
#
# print(sum_str("4", "5"))
# print(sum_str("34", "5"))

# вариант решения 2
# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))

# print(sum_str("4", "5"))

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

# def reverse_words(s):
#     return " ".join(s.split()[::-1])

# def reverse_words(s):
#     return ' '.join([i for i in s.split()[::-1]])

# def reverse_words(s):
#     list = s.split()
#     list = list[::-1]
#     return ' '.join(list)
#
# print(reverse_words("hello world"))

# Задача 3
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

# def powers_of_two(n):
#     return [2 ** res for res in range(n + 1)]

# print(powers_of_two(0))
# print(powers_of_two(1))
# print(powers_of_two(2))
# print(powers_of_two(3))

# def powers_of_two(n):
#     if n > 0:
#         return [2**num for num in range(n+1)]
#     else:
#         return [1]
#
# print(powers_of_two(0))
# print(powers_of_two(1))
# print(powers_of_two(2))
# print(powers_of_two(3))
