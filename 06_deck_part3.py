import random

# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠',
    'Clubs': '♣',
    'Diamonds': '♦',
    'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_uni = SUITS_UNI[suit]  # Масть карты картинка
        self.value_index = VALUES.index(value)  # Индекс значения карты для сравнения карт
        self.suit_index = SUITS.index(suit)  # Индекс масти карты для сравнения карт

    def to_str(self):
        return f'{self.value}{self.suit_uni}'

    def __str__(self):
        return f'{self.value}{self.suit_uni}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.value_index == other_card.value_index:
            return self.suit_index > other_card.suit_index
        return self.value_index > other_card.value_index

    def __gt__(self, other_card):
        if self.value_index == other_card.value_index:
            return self.suit_index > other_card.suit_index
        return self.value_index > other_card.value_index

    def less(self, other_card):
        return not self.more(other_card)

    def __lt__(self, other_card):
        return not self > other_card


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f'{self.__class__.__name__}[{len(self.cards)}]: {", ".join([card.to_str() for card in self.cards])}'

    def __str__(self):
        return f'{self.__class__.__name__}[{len(self.cards)}]: {", ".join([card.to_str() for card in self.cards])}'

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_in_hand = self.cards[:x]
        del self.cards[:x]
        return cards_in_hand

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, index):
        return self.cards[index]


deck = Deck()
deck.shuffle()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck.show())
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1.to_str())
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")
else:
    print(f"{card1} меньше {card2}")

# Это на следующее занятие.
# 4. Итерация по колоде:
for card in deck:
    print(card)

# 5. Просмотр карты в колоде по ее индексу:
# __getitem__(self, index):
print(deck[6])

# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
