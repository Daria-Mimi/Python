name = 'Daria'
age = 28
gender = 'female'

print (name, age, gender)

# print (type(name, age, gender))
# print не выведет типы (type) переменных, если они указаны через запятую (line 7)
# упадем с ошибкой (указана ниже)
# C:\Users\79017\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/79017/PycharmProjects/pythonProject/home_work_1.py
# Traceback (most recent call last):
#  File "C:\Users\79017\PycharmProjects\pythonProject\home_work_1.py", line 7, in <module>
#    print (type(name, age, gender))
# TypeError: type.__new__() argument 2 must be tuple, not int

# чтобы вывести каждый тип переменной, нужно к каждой переменной поставить функцию (type):
print (type(name), type(age), type(gender))
# при указании типа (type) только одной переменной, а остальных через "," без скобок, он выведет то, что указанно в переменных
print(type(name), age, gender)

# чтобы перевести один тип в другой - указываем какой тип хотим объявить той или иной переменной:
print (float(age), bool(gender))
