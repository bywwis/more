import math

class Triangle:
    def __init__(self, *edges):
        self.a = None
        self.b = None
        self.c = None
        match len(edges):
            case 1:
                self.a = self.b = self.c = edges[0]
            case 2:


            case 3:
                if edges[0] + edges[1] > edges[2] or edges[0] + edges[2] > edges[1] or edges[1] + edges[2] > edges[0]:
                    self.a, self.b, self.c = edges

    def info(self):
        if self.a is None:
            print('Такого треугольника не существует')
        print('Строны треугольника: ', self.a, self.b, self.c)


if __name__ == '__main__':
    tr1 = Triangle(5)
    tr1.info()
    tr2 = Triangle(10, 60)
    tr2.info()
    tr3 = Triangle(5, 6, 2)
    tr3.info()




