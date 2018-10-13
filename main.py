from card import *
from deck import Deck
from Table import Table
from game_manager import Game_manager

game_manager = Game_manager(3)
game_manager.deal_hands()
game_manager.print_state()


