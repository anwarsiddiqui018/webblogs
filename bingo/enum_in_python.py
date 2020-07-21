from enum import auto
from enum import Enum

# class Colour(Enum):
#     Red = 1
#     Green = 2
#     Blue = 3
class Colour(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

c = Colour.RED
# print(c)
# print(c.name)
print(c.value)
# print(c is Colour.Red)
# print(c is Colour.Blue)

# for name,member in Colour.__members__.items():
#     print(name,member)
    # Enumerations have a special attribute called __members__,
    # which is a read-only ordered mapping of names and members.
    # Utilising __members__ allows you to iterate over an enum and print
    # the members as well as their corresponding names.
