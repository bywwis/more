class Collector:
    def __init__(self):
        self.__d = dict()

    def collect(self, obj):
        if type(obj) not in self.__d.keys():
            self.__d[type(obj)] = [obj]
        else:
            self.__d[type(obj)] += [obj]

    def get_by_type(self, obj_type):
        if obj_type in self.__d.keys():
            return self.__d[obj_type]
        return []

    def __str__(self):
        print(self.__d)
        return ' '


if __name__ == '__main__':
    col = Collector()
    col.collect(1)
    col.collect(2)
    col.collect(3)
    col.collect([1, 2, 3, 4])
    col.collect([4, 5, 6])
    print(col.get_by_type(int))
    print(col.get_by_type(list))
    print(col)
