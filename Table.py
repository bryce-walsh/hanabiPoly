class Table:
  def __init__(self, played=None, discarded=None, max_hints=8):
    # if(played)
    #   self.played = played
    # else
    self.played = {"red":0,"green":0,"blue":0,"brown":0,"purple":0}
    # if(discarded)
    #   self.discarded = discarded
    # else
    self.discarded = {"red":[],"green":[],"blue":[],"brown":[],"purple":[]}
    self.bombs = 3
    self.hints = max_hints
    self.max_hints = max_hints


  def print_state(self):
    print("Played:")
    for key in self.played:
      print(str(self.played[key]) + " of " + key)
    print 
    print("Discarded: ")
    for key in self.discarded:
      print(key + ":")
      for number in self.discarded[key]:
        print(str(number)),
      print
    print("Hints:",self.hints)
    print("Bombs:",self.bombs)

  # Returns False if and only if they have run out of bombs
  def play(self, card):
    if (self.is_playable(card)):
      self.played[card.color] += 1
      if (self.played[card_color] >= 5):
        self.hints += 1
    else:
      self.bombs -= 1
      print("BOMB!")
      if (bombs <= 0):
        print("You lost (Too many bombs)")
        return False
      else:
         print("You have " + self.bombs + " bombs left!")
    return True

  def is_playable(self, card):
    playable = False
    if (self.played[card.color] == card.number - 1):
      playable = True  
    return playable

  # Returns True if discarding was allowed, false if not
  def discard(self, card):
    if (hints < max_hints):
      card_color = card.color
      array = self.discarded[card_color]
      array.append(card.number)
      array.sort()
      self.hints += 1
      return True
    else:
      return False

