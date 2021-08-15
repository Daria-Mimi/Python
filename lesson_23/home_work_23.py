
"""ДЗ сделать метод тумбочки таким, чтобы он мог работать принимая на вход как единичное значение, так и коллекцию:
множество, список или кортеж и выполнять то же самое действиве - добавление всех элементов в content.
Пример:
content = []
хочу добавить [1, 2, 3, 4, 5, 6] - все, что в списке сразу
Результат добавления:
content = [1, 2, 3, 4, 5, 6], а не [[1, 2, 3, 4, 5, 6], ]
"""
from datetime import datetime


class Tumbochka:
    def __init__(self):
        self.created_dt = datetime.now()
        self.content = []  # изначально тумбочка будет создаваться всегда пустая

    def add_into(self, subject):
        self.content.append(subject)
        for self.content in subject:
            print(*self.content)


    def __str__(self):
        return f"{self.content}"

    def __iter__(self):  # итератор - это то, что вернет этот метод. генератор - частный случай итератора.
        for el in self.content:
            yield el

tumbochka = Tumbochka()
a = 1
b = 2
c = 3
d = "TEST"
total = [a, b, c, d]
tumbochka.add_into(a)
tumbochka.add_into(b)
tumbochka.add_into(c)
tumbochka.add_into(d)
tumbochka.add_into(total)
print(tumbochka.content)
tumbochka.add_into([1, 2, "hello"])
print(tumbochka.content)