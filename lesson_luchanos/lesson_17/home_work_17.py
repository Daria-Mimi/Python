"""
Написать класс автомобиль с атрибутами: цвет, модель, год выпуска, количество л/с. У него должны быть методы ехать
вперед, назад, вправо, влево. При этом, если машина уже едет в том направлении, в котором её хочет послать пользователь
нужно выдавать информационное сообщение пользователю об этом. Кроме того, предусмотреть метод, который заводит машину
и который глушит её. На незаведенной машине ехать нельзя, о чем следует информировать пользователя. Также нельзя
заводить уже заведенную машину и глушить уже заглушенную.
"""

class Car:
    def __init__(self, model, color, power, year):
        self.model = model
        self.color = color
        self.power = power
        self.year = year
        self.launch = False
        self.vector = None

    def start(self):
        if self.launch:
            print(f"{self.model} is already started")
        else:
            self.launch = True
            print(f"{self.model} is started")

    def stop(self):
        if not self.launch:
            print(f"{self.model} is already muted")
        else:
            self.launch = False
            print(f"{self.model} is drowned out")

    def straight(self):
        if not self.launch:
            print("car is not started")
        elif self.vector == "straight":
            print(f"{self.model} is already going straight")
        else:
            print(f"{self.model} is going straight")
            self.vector = "straight"

    def back(self):
        if not self.launch:
            print("car is not started")
        elif self.vector == "back":
            print(f"{self.model} is already going back")
        else:
            print(f"{self.model} is going backwards")
            self.vector = "back"

    def left(self):
        if not self.launch:
            print("car is not started")
        elif self.vector == "left":
            print(f"{self.model} is already going to the left")
        else:
            print(f"{self.model} is goes to the left")
            self.vector = "left"


    def right(self):
        if not self.launch:
            print("car is not started")
        elif self.vector == "right":
            print(f"{self.model} is already going to the right")
        else:
            print(f"{self.model} is goes to the right")
            self.vector = "right"


suzuki = Car('vitara', 'red', 150, 2020)
suzuki.start()
suzuki.start()
suzuki.stop()
suzuki.straight()
suzuki.start()
suzuki.left()
suzuki.left()
suzuki.back()
suzuki.start()
suzuki.stop()
suzuki.left()
suzuki.start()
suzuki.right()
suzuki.right()
suzuki.right()
suzuki.right()