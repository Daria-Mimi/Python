# Задача 1
# l = [1, 2, 3, 4, 5]
# t = (2, 3, "test", "ololo", 5, 6)
# s = {5}
# print(s.intersection(t), s.intersection(l))
# print(set(l).intersection(t))
# print(set(t).intersection(s))

# # Задача 2
# res = []
# while True:
#     user = input("Введите произвольный элемент: ")
#     if user == "стоп":
#         break
#     res.append(user)

# print(res)

# ЗАДАЧА 3
# spisok = [1, -100, 10000, 0, 9, 1]
# user = int(input("Введите число: "))
# if user in spisok:
#     print(f"Число, которое Вы ввели {user} находится в списке на позиции {spisok.index(user)}")
# else:
#     print(f"Число, которое Вы ввели {user} в списке нет")

# Задача 1 через функцию
# l = [1, 2, 3, 4, 5]
# t = (2, 3, "test", "ololo", 5, 6)
# s = {5}
# # print(s.intersection(t), s.intersection(l))
#
# def some_funk(a, b):
#     res = set(a).intersection(b)
#     return res
#
# print(some_funk(l, t))

# ЗАДАЧА 3
# как нам сделать так, если у нас числа в нескольких позициях, чтобы он возвращал их все

# spisok = [1, -100, 10000, 0, 9, 1]
# res_position = []
# cnt = 0

# num = int(input("Введите число: "))
#
# for el in spisok:
#     if num == el:
#         res_position.append(cnt)
#     cnt += 1

# print(res_position)
