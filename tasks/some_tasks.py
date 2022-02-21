"""
Задача 1
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
Выведите все элементы, которые меньше 5.

Задача 2
Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

Задача 3
Отсортируйте словарь по значению в порядке возрастания и убывания.

Задача 4
Напишите программу для слияния нескольких словарей в один.

Задача 5
Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
"""

# 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for el in a:
#     if el < 5:
#         print(el)

# 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(filter(lambda elem: elem in b, a))
# result = [elem for elem in a if elem in b]
# print(result)

# 3
# d = {3: 4, 0: 0, 1: 2, 4: 3, 2: 1}
# import operator
# result = dict(sorted(d.items(), key=operator.itemgetter(1))) # в порядке возрастания
# print(result)

# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)) # в порядке убывания
# print(result)

# 4
# dict_a = {1: 10, 2: 20}
# dict_b = {3: 30, 4: 40}
# dict_c = {5: 50, 6: 60}

# result = {}
# for d in (dict_a, dict_b, dict_c):
#     result.update(d)
#     print(result)

# result = {**dict_a, **dict_b, **dict_c}
# print(result)

# 5
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)

# from heapq import nlargest
# result = nlargest(3, my_dict, key=my_dict.get)
# print(result)

