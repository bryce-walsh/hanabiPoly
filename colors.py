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