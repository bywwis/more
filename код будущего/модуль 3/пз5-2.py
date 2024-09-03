from overload import overload

class FloatRange:
    __start = 0
    __stop = 0
    __step = 1

    __current = None

    @overload
    def __init__(self, stop):
        self.__stop = stop

    @__init__.add
    def __init__(self, start, stop):
        self.__start = start
        self.__stop = stop

    @__init__.add
    def __init__(self, start, stop, step):
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __next__(self):
        if self.__current == None:
            self.__current = self.__start - self.__step
        if self.__current + self.__step < self.__stop and self.__step > 0:
            self.__current += self.__step
            return self.__current
        elif self.__step < 0 and self.__current + self.__step > self.__stop:
            self.__current += self.__step
            return self.__current
        else:
            self.__current = None
            raise StopIteration

    def __iter__(self):
        return self

if __name__ == '__main__':
    print([x for x in FloatRange(8, 0, -0.25)])


