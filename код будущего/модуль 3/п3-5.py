class Automobile:
    def __init__(self, capacity, max_speed, color):
        self.__capacity = capacity
        self.__max_speed = max_speed
        self.__color = color

        self.isEnginOn = False

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def get_color(self):
        return  self.__color

    def set_color(self, color):
        self.__color = color

    def enginON(self):
        self.__isEnginOn = True

    def enginOFF(self):
        self.__isEnginOn = False

    def drive(self):
        if self.__isEnginOn:
            print('---звуки наслаждения поездкой---')
        else:
            print('Нужно запустить двигатель для движения')

    def beep(self):
        return 'beep'

    def __del__(self):
        if not self.__isEnginOn:
            self.__color = None
            self.__capacity = None
            self.__max_speed = None
        else:
            print('Нельзя удалить, пока запущен двигатель')

class Car(Automobile):
    def beep(self):
        return super().beep() + 'beeeeep'

class SportCar(Car):
    def __init__(self, capacity, max_speed, color):
        super().__init__(capacity, max_speed, color)
        self.__isBoost = False

    def speedBoost(self):
        if not self.__isBoost:
            self.set_max_speed(self.get_max_speed() * (1 + len(self.get_color())/100))
            self.__isBoost = True

    def beep(self):
        return super().beep() + 'beeeeeeeeeeeeeeeeeeeeep!'


if __name__ == '__main__':
    sport_car = SportCar(2, 100, 'red')
    print(sport_car.beep())
    sport_car.speedBoost()
    print(sport_car.get_max_speed())
    sport_car.enginON()
    sport_car.drive()
    sport_car.enginOFF()
    sport_car.drive()


