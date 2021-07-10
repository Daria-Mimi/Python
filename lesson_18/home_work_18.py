"""
На основе ДЗ из 17 урока создать дочерние классы автомобилей (служебный, скорая помощь и т.д.). Я хочу, чтобы ты
реализовала метод, который будет проверять превышает ли автомобиль скорость, рекомендованную производителем.
По сути, чтобы был метод check_velocity, который говорил бы, превышаем мы скорость или нет.
"""

class Car:
    def __init__(self, model, color, power, year, speed):
        self.model = model
        self.color = color
        self.power = power
        self.year = year
        self.speed = speed
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

    def check_velocity(self):
        if self.speed > self.__class__.speed_limit:
            print(f"Вы превышаете скорость рекомендованную производителем {self.__class__.speed_limit}")

class Ambulance(Car):
    speed_limit = 90

    def __init__(self, model, color, power, year, speed):
        super().__init__(model, color, power, year, speed)


ambulance = Ambulance("GAZ", "red", 78, 2000, 98)
