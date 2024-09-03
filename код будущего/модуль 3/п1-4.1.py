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

    def __eq__(self, other):
        return (self.a * self.b == other.a * other.b
                and self.a == other.a
                and self.b == other.b)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return self.a * self.b <= other.a * other.b

    def __lt__(self, other):
        return self.a * self.b < other.a * other.b

    def __ge__(self, other):
        return self.a * self.b >= other.a * other.b

    def __gt__(self, other):
        return self.a * self.b > other.a * other.b


if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(3, 4)
    print(rect1 == rect2)
    rect3 = Rectangle(2, 4)
    print(rect1 > rect3)



