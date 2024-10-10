from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call _make_deck() in parent (or ancestor)
        for joker_num in 1, 2:
            joker_name = f"Joker{joker_num}"
            joker_card = Card(joker_name, joker_name)
            self._cards.append(joker_card)

if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(j1.cards)
    for _ in range(15):
        print(f"{j1.draw() = }")
    print()
    print(f"{j1 = }")
    print(j1)