"""
Задача 1
Напишите программу, которая принимает имя файла и выводит его расширение.
Если расширение у файла определить невозможно, выбросите исключение.

Задача 2
При заданном целом числе n посчитайте n + nn + nnn.

Задача 3
Напишите программу, которая выводит чётные числа из заданного списка и останавливается,
если встречает число 237.

Задача 4
Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

Задача 5
Сложите цифры целого числа.

Задача 6
Посчитайте, сколько раз символ встречается в строке.

Задача 7
Поменяйте значения переменных местами.

Задача 8
С помощью анонимной функции извлеките из списка числа, делимые на 15.
"""
# 1
# def get_extension(filename):
#     filename_parts = filename.split('.')
#     if len(filename_parts) < 2:  # filename has no dots
#         raise ValueError('the file has no extension')
#     first, *middle, last = filename_parts
#     if not last or not first and not middle:
#         # example filenames: .filename, filename., file.name.
#         raise ValueError('the file has no extension')
#     return filename_parts[-1]

# print(get_extension('abc.py'))
# print(get_extension('abc'))  # raises ValueError
# print(get_extension('.abc'))   # raises ValueError
# print(get_extension('.abc.def.'))   # raises ValueError
# print(get_extension('abc.txt'))
# print(get_extension('abc.prrr'))

# 2
# def solve(n):
#     n1 = n
#     n2 = int(str(n) * 2)
#     n3 = int(str(n) * 3)
#     print(n1 + n2 + n3)

# solve(5)

# 3
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# ]

# for x in numbers:
#     if x == 237:
#         break
#     elif x % 2 == 0:
#         print(x)

# 4
# set_1 = set([111, 246, 357])
# set_2 = set([246, 333])

# print(set_1 - set_2)

# 5
# def sum_digits(num):
#     digits = [int(d) for d in str(num)]
#     return sum(digits)

# print(sum_digits(5245))


# 6
# string = 'Python Software Foundation'
# print(string.count('t'))

# 7
# x = 5
# y = 10
# x, y = y, x
# print(x, y)

# 8
nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))

