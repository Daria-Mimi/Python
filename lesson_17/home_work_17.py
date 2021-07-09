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
        self.direction_1 = None
        self.direction_2 = None
        self.direction_3 = None
        self.direction_4 = None

    def start(self):
        if self.launch:
            print(f"{self.model} is already started")
        else:
            print(f"{self.model} is started")
            self.launch = True

    def stop(self):
        if not self.launch:
            print(f"{self.model} is already muted")
        else:
            print(f"{self.model} is drowned out")
            self.launch = False

    def straight(self):
        if not self.launch:
            print("car is not started")
        elif self.direction_1:
            print(f"{self.model} is already going straight")
        else:
            print(f"{self.model} is going straight")
            self.direction_1 = True

    def back(self):
        if not self.launch:
            print("car is not started")
        elif self.direction_2:
            print(f"{self.model} is already going back")
        else:
            print(f"{self.model} is going backwards")
            self.direction_2 = True

    def left(self):
        if not self.launch:
            print("car is not started")
        elif self.direction_3:
            print(f"{self.model} is already going to the left")
        else:
            print(f"{self.model} is goes to the left")
            self.direction_3 = True


    def right(self):
        if not self.launch:
            print("car is not started")
        elif self.direction_4:
            print(f"{self.model} is already going to the right")
        else:
            print(f"{self.model} is goes to the right")
            self.direction_4 = True


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