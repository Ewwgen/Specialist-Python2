class Card:
    def __init__(self, suit, index):
        self.suit = suit
        self.index = index
    #https://unicode-table.com/ru/#basic-latin
    def to_str(self):
        str_suit = ''
        if self.suit == 'Hearts':
            str_suit = '\u2661'
        elif self.suit == 'Spades':
            str_suit = '\u2660'
        elif self.suit == 'Diamonds':
            str_suit = '\u2662'
        elif self.suit == 'Clubs':
            str_suit = '\u2663'
        print(self.index+str_suit)

    def equal_suit(self, other):
        return self.suit == other.suit

    def more(self, other):
        index_rank = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, 'A':12}
        return index_rank[self.index]>index_rank[other.index]

    def less(self, other):
        index_rank = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, 'A':12}
        return index_rank[self.index]<index_rank[other.index]

card01 = Card('Hearts','J')
card01.to_str()

card02 = Card('Clubs','2')
card02.to_str()

card03 = Card('Diamonds','A')
card03.to_str()

card04 = Card('Spades','Q')
card04.to_str()

card05 = Card('Spades','10')
card05.to_str()

print('Проверка метода equal_suit: ')
print(card01.equal_suit(card02))
print(card04.equal_suit(card05))
print('Проверка метода more: ')
print(card02.more(card05))
print(card04.more(card01))
print(card03.more(card02))
print('Проверка метода less: ')
print(card02.less(card05))
print(card04.less(card01))
print(card03.less(card02))


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        index_rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits_rank = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

        for suit in suits_rank:
            for ind in index_rank:
                # Card(suit, ind).to_str()
                self.cards.append(Card(suit, ind))

deck = Deck()
print(deck[0])

