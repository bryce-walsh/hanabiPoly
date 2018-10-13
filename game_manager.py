from card import *
from deck import Deck
from Table import Table

def cards_per_player(num_players):
  if num_players == 2:
    return 5
  if num_players == 3:
    return 5
  if num_players == 4:
    return 4
  if num_players == 5:
    return 4
  raise ValueError('Invalid number of players: ' + str(num_players))

class Game_manager:

  def __init__(self, num_players):
    self.num_players = num_players
    self.hand_size = cards_per_player(num_players)
    self.table = Table()
    self.deck = Deck()
    self.hands = []

  def print_state(self):
    print("Current Hands:")
    if self.hands == []:
      print("Hands not dealt")
    else:
      for hand in self.hands:
        print(hand)
    print()
    print("Current Table:")
    self.table.print_state()
    print()

  def deal_hands(self):
    for hand in range(0,self.num_players):
      self.hands.append(self.deck.draw(self.hand_size))

  def print_visible_hands(self, player_number):
    for hand_num in range(0,self.num_players):
      if hand_num != player_number:
        print(self.hands[hand_num])

  def play_game(self):
    for turn in range(0, 100):
      player_number = turn % self.num_players
      print("It is player " + str(player_number) + "'s turn")
      print("Visible_hands:")
      self.print_visible_hands(player_number)
      response = input("What would you like to do?")
