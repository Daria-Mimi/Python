"""ДЗ 4 Глава
Учить приведение типов!!! Как отче наш!!!
Решать задачи!!!
ЗАДАЧИ:
1. Написать программу, которая бы запрашивала у пользователя число в десятичной
системе счисления и возвращала бы его запись в двоичной системе счисления. Перевод
с помощью встроенных функций будет считаться читом - пользуйся арифметическими
операциями)
2. Пользователь вводит число. Найти самую большую цифру в этом числе и вывести
её на экран.
ПРАКТИЧЕСКАЯ РАБОТА:
сравнить между собой строки и объяснить результат:
'123' и '1234'
'abc' и 'abcd'
'a123' и '123'
'abc' и ''
Привести к типу bool и посмотреть что получится:
1, '1', 0, '0', ''
"""

from time import sleep

# Если бы нас попросили многократно выводить одно и то же
# print(10)
# print(10)
# print(10)
# print(10)
# print(10)
# print(10)
# print(10)


# Способ вывода через цикл
# До тех пор, пока соблюдается условие мы крутим вертим цикл
cnt = 0
# limit = 7
# name = 'My name is Nikolai'

# print(1 * 100 < 2 - 10)

# бесконечный цикл
# while True:
# конечный цикл

# изменение значения переменной относительно самой себя
# cnt = cnt + 1
# cnt = cnt + 1
# cnt = cnt + 1

# более короткий способ
# cnt += 1


# while cnt <= limit:
#     sleep(.5)
#     print(cnt, name)
#     cnt = cnt + 1

# name = input("Введите своё имя:")
# print(name == 'Коля')

# s = "100000000000"
# i = int(s)


# limit = int(input("Введите количество желаемых циклов: "))

# while cnt <= limit:
#     print(cnt, input("Введите своё имя: "))
#     cnt = cnt + 1
# limit = int(limit)

name_1 = 'Николай'
name_2 = 'Даша'
name_3 = 'Мосес'

current_name = 'Асланбек 1'
current_name_2 = 'Николай'
current_name_3 = 'Даша'
current_name_4 = 'Мосес'

name_for_eq = current_name_4

# if name_1 == name_for_eq or name_2 == name_for_eq or name_3 == name_for_eq:
#     print("привет, Друг!")
# else:
#     print("Не брат ты мне!")

if name_1 == name_for_eq:
    print(f"привет, {name_1}!")
elif name_2 == name_for_eq:
    print(f"привет, {name_2}!")
elif name_3 == name_for_eq:
    print(f"привет, {name_3}!")
else:
    print("Не брат ты мне!")
