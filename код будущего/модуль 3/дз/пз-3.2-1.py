class TypeHunter:
    def __init__(self):
        self.__d = dict()

    def get_by_type(self, obj_type):
        if obj_type in self.__d.keys():
            return self.__d[obj_type]
        return []

    def filter(self, collection, target_type):
        result = [obj for obj in collection if isinstance(obj, target_type)]
        obj_type = target_type.__name__
        if obj_type in self.__d:
            self.__d[obj_type] += len(result)
        else:
            self.__d[obj_type] = len(result)
        return result

    def show_stats(self):
        for obj_type, count in self.__d.items():
            print(f"Найдено объектов типа {obj_type}: {count}")

if __name__ == '__main__':
    col = TypeHunter()
    col.filter(1, int)
    col.filter(2, int)
    col.filter(3, int)
    col.filter([1, 2, 3, 4], list)
    col.filter([4, 5, 6], list)
    print(col.get_by_type(int))
    print(col.get_by_type(list))
    print(col)

