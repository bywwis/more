class Computer:
    def __init__(self):
        self.is_power = False

    def build(self, proc, video, ram, hdd):
        self.proc = proc
        self.video = video
        self.ram = ram
        self.hdd = hdd
        self.is_power = True

    def power_on(self):
        return self.is_power

if __name__ == '__main__':
    comp = Computer()
    print(comp.power_on())
    comp.build('i7', 'GTX 4090', 32, 1000)
    print(comp.power_on())