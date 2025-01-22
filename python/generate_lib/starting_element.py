from .Segment import *
from .miscellaneous import rotate60

# returns starting element based on conditions
def starting_element(conditions):
    if 1: # berb berb
        element = [Segment(0, 0, 0, 1)]
        for i in range(5):
            element.append(rotate60(element[-1]))
    if 0: # berb berb
        print("berb")
    return [element]