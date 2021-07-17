"""
На основе ДЗ из 17 урока создать дочерние классы автомобилей (служебный, скорая помощь и т.д.). Я хочу, чтобы ты
реализовала метод, который будет проверять превышает ли автомобиль скорость, рекомендованную производителем.
По сути, чтобы был метод check_velocity, который говорил бы, превышаем мы скорость или нет.
"""

class Car:
    speed_limit = 0

    def __init__(self, model, color, power, year, speed):
        self.model = model
        self.color = color
        self.power = power
        self.year = year
        self.speed = speed
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

    def check_velocity(self):
        if self.speed > self.__class__.speed_limit:
            print(f"Вы превышаете скорость рекомендованную производителем {self.__class__.speed_limit}")

class Ambulance(Car):
    speed_limit = 90

    def __init__(self, model, color, power, year, speed):
        super().__init__(model, color, power, year, speed)
        self.sirena = None

    def on_sirena(self):
        if self.sirena == "Sirena on":
            print("Sirena is already on")
        else:
            self.sirena = "Sirena on"
            print("Sirena on")

    def off_sirena(self):
        if self.sirena == "Sirena off":
            print("Sirena is already off")
        else:
            self.sirena = "Sirena off"
            print("Sirena off")



ambulance = Ambulance("GAZ", "red", 78, 2000, 98)
ambulance.on_sirena()
ambulance.on_sirena()
ambulance.on_sirena()
ambulance.off_sirena()
ambulance.off_sirena()

