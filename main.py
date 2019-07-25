import random
import itertools
import dataclasses

SUIT = ["H", "C", "D", "S"]
NUMBER = range(1, 14)
CARDS = list(itertools.product(SUIT, NUMBER)) + [('J', 0)]

@dataclasses.dataclass
class Card():
    suit: str
    number: int
    is_joker: bool = False


class Table():
    def __init__(self):
        self.cards = []
        self.setRandomCards(5)
        self.hand = None
        self.cards = self.getSortedTable()
        self.getHand()

    def __repr__(self):
        return '<Table cards={0.cards}>'.format(self)

    def setRandomCards(self, count):
        self.cards += [self.getCard(i) for i in random.sample(CARDS, k=count)]
        return self.cards

    def getCard(self, name):
        return Card(name[0], name[1], name[0] == "j")

    def getSortedTable(self):
        return sorted(self.cards, key=lambda card: card.number)

    def getHand(self):
        self.hand = Hand(self.cards)


@dataclasses.dataclass
class Hand():
    cards: list

    def __post_init__(self):
        self.getTopHand()

    def getTopHand(self):
        print(self.cards)


if __name__ == "__main__":
    table = Table()
    print(table)