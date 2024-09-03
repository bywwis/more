class Figure:
    def __init__(self):
        self.__verticies = None
        self.__edges = None

    def get_verticies(self):
        return self.__verticies

    def set_verticies(self, verticies):
        self.__verticies = verticies

    def get_edges(self):
        return self.__edges

    def set_edges(self, edges):
        self.__edges = edges

    def perimetr(self):
        # полиморфизм - задание 3
        if isinstance(self, Figure) and not isinstance(self, (Square, Triangle)):
            return None
        elif isinstance(self, Square):
            return 4 * self.get_a()
        elif isinstance(self, Triangle):
            return sum(self.get_sides())
        else:
            return None

    def area(self):
        if isinstance(self, Figure) and not isinstance(self, (Square, Triangle)):
            return None
        elif isinstance(self, Square):
            return  self.get_a() ** 2
        elif isinstance(self, Triangle):
            p = self.perimetr() / 2
            S = (p * (p-self.get_sides()[0]) * (p-self.get_sides()[1]) * (p-self.get_sides()[2])) ** 0.5
            return S
        else:
            return None

    def __str__(self):
        if isinstance(self, Figure) and not isinstance(self, (Square, Triangle)):
            return f"Количество вершин: {self.__verticies}, количество рёбер: {self.__edges}"
        elif isinstance(self, Square):
            return f"Количество вершин: {self.__verticies}, количество рёбер: {self.__edges}, Сторона - {self.get_a()}"
        elif isinstance(self, Triangle):
            return f"Количество вершин: {self.__verticies}, количество рёбер: {self.__edges}, Стороны: {', '.join(map(str, self.get_sides()))}"
        else:
            return None


class Square(Figure):
    def __init__(self, a):
        self.__a = a
        super().set_verticies(4)
        super().set_edges(4)

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    #def perimetr(self):
    #    return 4 * self.__a

    #def area(self):
    #    return self.__a ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().set_verticies(3)
        super().set_edges(3)
        self.__sides = [a, b, c]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *a):
        self.__sides = a

    #def perimetr(self):
    #    return sum(self.__sides)

    #def area(self):
    #    p = self.perimetr() / 2
    #    S = (p * (p-self.__sides[0]) * (p-self.__sides[1]) * (p-self.__sides[2])) ** 0.5
    #    return S




if __name__ == '__main__':
    # задание 1
    fig1 = Figure()
    print(fig1)
    fig1.set_edges(4)
    fig1.set_verticies(4)
    print(fig1)

    # задание 2, 3
    sq = Square(5)
    print(sq)
    print(f'P = {sq.perimetr()}, S = {sq.area()}')

    tri = Triangle(2, 4, 5)
    print(tri)
    print(f'P = {tri.perimetr()}, S = {tri.area()}')






















