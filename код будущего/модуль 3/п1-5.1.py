class CardStack:
    def __init__(self, cards):
        self.cards = cards

    def __add__(self, other): # складывать колоду
        return CardStack(list(set(self.cards + other.cards)))

    def __sub__(self, other): # вычитать колоду
        return CardStack(list(set(self.cards) - set(other.cards)))

    def __neg__(self): #брать отрицание из колоды
        card_base = ['2', '3', '4', '5', '6', '7', '8', '9', 'V', 'D', 'K', 'T']
        return CardStack(list(set(card_base) - set(self.cards)))

if __name__ == '__main__':
    cards1 = CardStack(['2', '3', '5'])
    cards2 = CardStack(['4', '5', '7', '8', '9', 'D'])

    cards_new = cards1 + cards2
    print(cards_new.cards)

    cards_new = cards1 - cards2
    print(cards_new.cards)

    cards_new = cards2.__neg__()
    print(cards_new.cards)

