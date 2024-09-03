class AirShip:
    def __init__(self, max_mass, speed_flight):
        self.__max_mass = max_mass
        self.__speed_flight = speed_flight

        self.__isTakeOffPlane = False

    def get_max_mass(self):
        return self.__max_mass
    def set_max_mass(self, max_mass):
        self.__max_mass = max_mass

    def get_speed_flight(self):
        return self.__speed_flight
    def set_speed_flight(self, speed_flight):
        self.__speed_flight = speed_flight

    def TakeOff(self):
        self.__isTakeOffPlane = True

    def TakeOn(self):
        self.__isTakeOffPlane = False

    def Flight(self):
        if self.__isTakeOffPlane:
            print('---температура за бортом хорошая, наслаждайтесь полётом---')
        else:
            print('Нужно взлететь')

    def Signal(self):
        return '12345'


class AirPlain(AirShip):
    def Signal(self):
        return super().Signal() + '6897'


class AirJet(AirPlain):
    def __init__(self, max_mass, speed_flight):
        super().__init__(max_mass, speed_flight)
        self.__isBoost = False

    def speedBoost(self):
        if not self.__isBoost:
            self.set_speed_flight(self.get_speed_flight() + (self.get_speed_flight() * 0.05))
            self.__isBoost = True

    def Signal(self):
        return super().Signal() + '111111'

if __name__ == '__main__':
    air_jet = AirJet(3000, 800)
    print(air_jet.Signal())
    air_jet.speedBoost()
    print(air_jet.get_speed_flight())
    air_jet.TakeOff()
    air_jet.Flight()
    air_jet.TakeOn()
    air_jet.Flight()


