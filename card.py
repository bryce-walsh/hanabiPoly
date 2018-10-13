from enum import Enum
class Color(Enum):
  RED = 1
  YELLOW = 2
  GREEN = 3
  BLUE = 4
  WHITE = 5

  def __str__(self):
    return {
        Color.RED: "Red",
        Color.YELLOW: "Yellow",
        Color.GREEN: "Green",
        Color.BLUE: "Blue",
        Color.WHITE: "White"
    }[self]

class Card:

  def __init__(self, color, number):
    self.color = color
    self.number = number

  def __str__(self):
    return (str(self.number) + " of " + str(self.color))

  def __repr__(self):
    return self.__str__()