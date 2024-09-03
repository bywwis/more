class Joiner:

    @staticmethod
    def Join(delimiter, objects):
        result = ''
        for obj in objects:
            if isinstance(obj, (str, int, float)):
                result += delimiter + str(obj)
            elif isinstance(obj, (list, set, tuple)):
                result += delimiter + Joiner.Join(delimiter, obj)

        return result.replace(delimiter, '', 1)

if __name__ == '__main__':

    obj = [1, [1, 2, 3], [[4, 5], [6, 7]], 8, '1223']
    print(Joiner.Join(", ", obj))



