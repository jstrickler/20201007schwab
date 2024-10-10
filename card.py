class Card:
    # inherits __init__() and __repr__() from 'object' if not implemented
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property  # decorators start with "@"
    def rank(self):
        return self._rank
    # rank = property(rank)
    # new_rank = property(rank)

    @property
    def suit(self):
        return self._suit
    
    # 8-Diamonds   A-Spades 2-Clubs
    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card("8", "Diamonds")  # args to constructor (__init__)
    print(f"{c = }")
    c2 = Card("A", "Spades")
    print(f"{c.rank = }")
    print(f"{c.suit = }")

    print(c)   #  str()
    print(f"{c = }")   #  repr()
    

    
