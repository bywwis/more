class ShoppingList:
    items = []

    def __init__(self, it):
        self.items = list(it)

    def __repr__(self):
        if len(self.items) == 0:
            return 'Этот список пуст'
        else:
            return f'Этот список из {len(self.items)} позиций:\n {"/n".join(self.items)}'


    def __str__(self):
        if len(self.items) == 0:
            return 'Этот список пуст'
        else:
            return f"Этот список из {len(self.items)} позиций:\n {'\n'.join(list(sorted(self.items)))}"

if __name__ == '__main__':
    list_shop = ShoppingList(['milk', 'sugar', 'butter', 'bread'])
    print(list_shop) # __str__
    temp = [list_shop]
    print(temp) # __repr__