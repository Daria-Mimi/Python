# name = 'Daria'
# surname = "Mishankova"
# patronymic = 'Andreevna'
# КОНКАТЕНАЦИЯ
# print(surname + ' ' + name + ' ' + patronymic)

# Метод .format
# print({surname} {name} {patronymic}.format)
# вылезла ошибка, тк не поставили "" - строку, в методе формат не указали аргументы
# C:\Users\79017\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/79017/PycharmProjects/pythonProject/home_work_2.py
#   File "C:\Users\79017\PycharmProjects\pythonProject\home_work_2.py", line 8
#     print({surname} {name} {patronymic}.format)
#                     ^
# SyntaxError: invalid syntax
#
# Process finished with exit code 1

# print('{} {} {}'.format(surname, name, patronymic))
# если хотим изменить очередность вывода, вводим следующим образом:
# print('{1} {2} {0}'.format(surname, name, patronymic))

# способ 2
# seats = 50
# some_str = '%s количество свободных мест в зале %d' % (name, seats)
# print(some_str)

# способ 3 F/f
# some_str_2 = f'Hello! My name is {name}'
# print(some_str_2)

# question = input('Как тебя зовут? ')
# name_1 = "Дарья"
# print(question == "Дарья")
# if question == name_1 :
#    print(f'Добрый день, {name_1}' )
# else: print("Не угадал!")

# a = 123 + 222
# b = 1.5 * 4
# c = 2 ** 100
# print(a, b, c)

# d = len(str(2 ** 1000000)) # len - функция подсчета количества символов/цифр в итоговой строке (кол-во 301030)
# print(d)

# S = 'Spam'  # Создать 4-символьную строку и присвоить ее некоторому имени
# print(len(S))
# ответ 4 - Длина
# print(S[0], S[1], S[2], S[3]) # 1-й элемент,который индексируется [] по позиции, начиная с нуля (слево на право - по порядку)
# print(S[-1], S[-2], S[-3], S[-4]) # Последний элемент с конца !!! но начинается не с 0, а с 1
# выводит сдедующее:
# S p a m
# m a p S

# a_1 = S[1:] # Все после первого элемента (1: len (S)) - pam
# b_1 = S[0:3] # Все кроме последнего элемента - Spa
# c_1 = S[:3] # То же, что и S[0:3] - Spa
# d_1 = S[:-1]  # Снова все кроме последнего элемента, но проще (0:-1) - Spa
# e_1 = S[:] # Вся строка S как копия верхнего уровня (0: len(S)) - Spam
# print(a_1, b_1, c_1, d_1, e_1)

# S = 'Spam'
# S = 'z' + S[1:] # можем выполнить выражения для создания новых объектов
# print(S)

# S = 'shrubbery'
# L = list(S) # Развернуть в список: [. . . ]
# print(L)

# L[1] = 'с' # Изменить на месте
# ''.join(L) # Объединить с пустым разделителем
# print(L)

# sp = "Spam"
# fi = sp.find('pa') # Найти смещение подстроки в sp
# print(fi)

# re = sp.replace('pa', 'PRO') # Заменить вхождения подстроки в sp другой подстрокой
# print(re)

# line = 'ааа,bbb,ссссс,dd'
# li = line. split (', ') # Разбить по разделителю в список подстрок
# print(li)

# sp_1 = sp.upper() # Преобразовать в верхний и нижний регистры
# print(sp_1)

# isa = sp_1.isalpha() # Проверить содержимое: isalpha, isdigit и т.д.
# print(isa)

# line = 'ааа,bbb,ссссс,dd\n'
# li = line.rsplit() # Удалить пробельные символы с правой стороны
# print(li)

# li_1 = line.rsplit() + line.split(',') # Скомбинировать две операции
# print(li_1)

# a = []  # заводим пустой список
# n = int(input())  # считываем количество элемент в списке
# for i in range(n):
#     new_element = int(input())  # считываем очередной элемент
#     a.append(new_element)  # добавляем его в список
#     # последние две строки можно было заменить одной:
#     # a.append(int(input()))
# print(a)

# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# d_1 = D['food'] # Извлечь значение, связанное с ключом 'food'
# print(d_1)

# D = {}
# D['name'] = 'Bob' # Присваивание приводит к созданию ключей
# D['job'] = 'dev'
# D['age'] = 40
# print(D)
# print(D['name'])
