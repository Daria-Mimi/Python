# 1. Хотим получить список чисел от 0 до 1_000_000,
# но в конечном списке должно быть только каждое третье число из этого диапазона.

# решение 1
# res = []
# cnt = 0
# while cnt <= 100:
#     if cnt % 3 == 0:
#         res.append(cnt)
#     cnt +=1
#
# print(res)

# решение 2
# res1 = [res for res in range(100) if res % 3 == 0]
# print(res1)

# 2. Запрашиваем у пользователя числа, разделенных пробелом и записываем их в список, предварительно переведя каждое из
# них в целочисленный тип. Пример пользовательского ввода: 1 2 3 100 -99.
# Дальше нужно собрать из списка строку, в которой бы содержались только чётные числа из этого списка в порядке по
# возрастанию и разделенные тем сообщением, которое введет пользователь.

# res = []
# cnt = 0
# user = input("Введите произвольные числа через пробел: ").split()
# for el in user:
#     res.append(int(el))
#
# print(res)
#
# res1 = [x for x in res if x % 2 == 0]
# print(res1)
#
# user2 = input("Введите символ, который хотите использовать в качестве разделителя: ")
# string = f'{user2}'.join(str(x2) for x2 in sorted(res1))
# print(string)


# 3. Написать бинарный поиск для отсортированного листа.
# def binarysearch(a, b):
#     if len(a) == 0:
#         return False
#     else:
#         midpoint = len(a) // 2
#         if a[midpoint] == b:
#             return True
#         else:
#             if b < a[midpoint]:
#                 return binarysearch(a[:midpoint],b)
#             else:
#                 return binarysearch(a[midpoint+1:],b)

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(binarysearch(list, 3))
# print(binarysearch(list, 5))

# 4. Запрашиваем у пользователя произвольные строки до тех пор, пока он не введет СТОП. Строки складываем в файл с учетом
# того, что каждую новую введенную пользователем строку нужно переносить. При этом перед открытием файла спрашивать у
# пользователя, хочет ли он дозаписывать существующую инфу в файле или зачищать.

data = ""
mode_mapper = {"дозаписать": "a", "очистить": "w"}
mode = input("Вы хотите очистить файл или дозаписать?: ")
file = open("home_work_10.txt", mode=mode_mapper[mode])

while True:
    data = input("Введите строчку: ") + "\n"
    if data[:-1] == "стоп":
        break
    file.write(data)







# res = ""
# user = input("Вы хотите дозаписать файл или очистить его полностью?: ")

# while True:
#     user = input("Вы хотите дозаписать файл или очистить его полностью?: ")
#     if user == "дозаписать":
#         file = open("home_work_10.txt", mode="a")
#         file.writelines(input("Введите строку: "))
#     elif user == "очистить":
#         file = open("home_work_10.txt", mode="w")
#         file.write(input("Введите строку: "))
#     elif user == "стоп":
#         break
# print(open("home_work_10.txt", mode="r"))
