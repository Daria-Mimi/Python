# Принимаем на вход строку произвольного текста. Нужно заменить каждый третий символ на *.
# some_string = input("Введите строку: ")
# cnt = 0
# res = ""
# while cnt < len(some_string):
#     if cnt % 3 == 0:
#         res += "*"
#     else:
#         res += some_string[cnt]
#     cnt += 1
# print(res)

# Пользователь вводит число. Найти самую большую в этом числе и вывести на экран.
# some_string = int(input("Введите число: ")) # 102637
# max_num = 0
# work = some_string
# while work > 0:
#     res = work % 10
#     if res > max_num:
#         max_num = res
#     work //= 10
# print(max_num)

# Пользователь вводит число. Найти самую меньшую в этом числе и вывести на экран.
# some_string = int(input("Введите число: ")) # 12984
# work = some_string
# num_min = 9
# while work > 9:
#     res = work % 10
#     if res < num_min:
#         num_min = res
#     work //= 10
# print(num_min)


# из методички
# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
# a = "Привет, друг!"
# print(a)
# b = input("Введите предложение: ")
# c = int(input("Введите число: "))
# print(b, c)

# 2.Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# time = int(input("Введите время в секундах: "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

# 3.	Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# n = int(input("Введите число - "))
# n1 = int(str(n) + str(n))
# n2 = int(str(n) + str(n) + str(n))
# total = (n + n1 + n2)
# print(f"Сумма чисел {n} + {n1} + {n2} = %d" % total)

# 4.	Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
# user = int(input("Введите целое число: "))
# num_for_work = user
# max_num = 0
# while num_for_work > 0:
#     res = num_for_work % 10
#     if res > max_num:
#         max_num = res
#     num_for_work //= 10
# print('максимальное число из {} это {}'.format(user, max_num))

# 5.	Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
# proceeds = float(input("Введите выручку фирмы в рублях: "))
# loss = float(input("Введите убыток фирмы в рублях: "))
# if proceeds > loss:
#     res = proceeds / loss
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {res} %")
#     staff = int(input("Введите количество сотрудников фирмы: "))
#     print(f"Прибыль в расчете на одного сторудника сотавила: {proceeds / staff} рублей")
# elif loss == proceeds:
#     print("Фирма работает в ноль")
# else:
#     print(f"Фирма работает в убыток - {proceeds / loss} %")

# 6.	Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = float(input("Введите результаты пробежки первого дня в км: "))
b = float(input("Введите желаемый результат в км: "))
res_day = 1
res_km = a
while a < b:
        a = a + a * 0.1
        res_day += 1
        res_km += res_km
print(f"Вы достигнете желаемого результата на %.d день" % res_day)
