import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []  # make a list of cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        # handle empty deck here...
        return self._cards.pop()
    
    def __len__(self):  # implents len() for this class
        return len(self._cards)
    
    def __str__(self):
        #  CardDeck/45
        my_type = type(self)
        return f"{my_type.__name__}/{len(self)}"

    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"

if __name__ == "__main__":
    d1 = CardDeck()
    d1.shuffle()
    print(d1.cards)
    print()
    for _ in range(7):
        print(d1.draw())

    # len(obj)
    print(f"{len(d1) = }\n")
    print(d1)
    print(f"{d1 = }")
    
    # len(d1)
    # CardDeck.__len__(d1)
    # def len(obj):
    #    type(obj).__len__(obj)