# задача 1
# some_number = int(input('Введите число: ')) # 122
# определяем переменную, сразу делаем приведение типов, запрашиваем из консоли число
# print(some_number % 2) # влетела на ошибку, тк из консоли возвращается текст, а не число
# decision = '' # организовали строку, куда будут сохранять остатки при делении
# while some_number > 0:
#     decision = str(some_number % 2) + decision
#     some_number //= 2
# print(decision) # ответ 1111010

# задача 2
# user = int(input('Ввведите число: ')) # например число 12345098
# num_for_work = user
# max_num = 0
# while num_for_work > 0:
#     res = num_for_work % 10
#     if res > max_num:
#         max_num = res
#     num_for_work //= 10
# print('максимальное число из {} это {}'.format(user, max_num))

# задача № 3
# ex = '123' == '1234' # False
# ex1 = 'abc' < 'abcd' # True
# ex2 = 'a123' != '123' # True
# ex3 = 'abc' > '' # True
# ex4 = 'A' > 'a'
# ex5 = ord("A")
# ex6 = ord("a")
# print(ex, ex1, ex2, ex3, ex4)
# print(ex5, ex6)

# задача 4 Практическая работа
# a = bool(1)
# b = bool("1")
# c = bool(0) # ноль всегда False
# d = bool("0")
# e = bool("") # пустая строка поэтому False
# print(a, b, c, d, e)
# если в строке что-то есть, это всегда True
