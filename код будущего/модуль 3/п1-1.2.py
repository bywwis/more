class Airplane:
    is_fly = False

    def board(self, passangers):
        self.passangers = passangers
        self.is_fly = True

    def flight(self):
        return self.is_fly

if __name__ == '__main__':
    ap = Airplane()
    print(ap.flight())
    ap.board(['fio1', 'fio1', 'fio3'])
    print(ap.flight())
