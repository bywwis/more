class Rectangle:
    def __init__(self, *edges):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        match len(edges):
            case 1:
                self.a = self.b = self.c = self.d = edges[0]
            case 2:
                self.a = self.c = edges[0]
                self.b = self.d = edges[1]
            case 4:
                if edges[0] + edges[2] == edges[1] + edges[3]:
                    self.a, self.b, self.c, self.d = edges

    def info(self):
        if self.a is None:
            print('Четырехугольника не существует')
        print('Стороны 4-х угольника: ', self.a, self.b, self.c, self.d)

if __name__ == '__main__':
    rect1 = Rectangle(10)
    rect1.info()
    rect2 = Rectangle(5, 10)
    rect2.info()
    rect3 = Rectangle(1, 4, 5, 2)
    rect3.info()


