from card import *
from deck import Deck
from table import Table

card = Card(Color.BLUE, 5)
print(card)
table = Table()
table.print_state()


deck = Deck()
deck.print_deck()
