"""
- Запрашиваем у пользователя данные о юзерах: имена, фамилии, адреса, года рождения. Формируем словари и записываем их
в json-файл. То есть мы последовательно запрашиваем у пользака с экрана данные о других людях. Если мы хотим прекратить
ввод данных, то надо задать этот вопрос в соответствующем месте и обработать стоп-слово. С дозаписью разберись сама *.
установить json-viewer в Пайчарм и Хром
- Дополнить класс автомобиля так, чтобы его можно было использовать в менеджере контекста: при передаче в него объекта
автомобиль нужно включать зажигание, а при выходе - выключать.
"""
import json

data = dict()

print("Введите команду для записи данных в файл или завершение работы с ним.")
print("стоп - завершить работу с файлом\n"
      "1 - записать в файл")

while True:
    user_choice = input("Введите ваш выбор: ")
    if user_choice == "1":
        data['name'] = input("Enter name: ")
        data['surname'] = input("Enter surname: ")
        data['date_of_Birth'] = int(input("Enter date of Birth: "))
    elif user_choice == "стоп":
        break

with open("user_data.json", "w") as json_obj:
    json.dump(obj=data, fp=json_obj)