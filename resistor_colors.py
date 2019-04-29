from enum import Enum
from collections import deque

class ResistorValueColor(Enum):
    BLACK  = 0
    BROWN  = 1
    RED    = 2
    ORANGE = 3
    YELLOW = 4
    GREEN  = 5
    BLUE   = 6
    VIOLET = 7
    GREY   = 8
    WHITE  = 9

class ResistorMultiplierColor(Enum):
    SILVER = 0.01
    GOLD   = 0.1
    BLACK  = 1
    BROWN  = 10
    RED    = 100
    ORANGE = 1000
    YELLOW = 10000
    GREEN  = 100000
    BLUE   = 1000000
    VIOLET = 10000000

class ResistorToleranceColor(Enum):
    BROWN  = 1
    RED    = 2
    GREEN  = 0.5
    BLUE   = 0.25
    VIOLET = 0.1
    GOLD   = 5
    SILVER = 10
    NONE   = 20

def _all_zeros(arr):
    for a in arr:
        if a != 0:
            return False
    return True

def resistor_color_bands(value, num_bands=4, tolerance=1):
    if value == 0:
        return []

    num_digit_bands = num_bands - 2 # 1 multiplier band and 1 tolerance band
    multiplier = 1

    if num_digit_bands < 1:
        raise Exception("not enough bands")

    # Convert to integer so we don't have to deal with decimal places,
    # adjusting multiplier as necessary
    v = value
    while True:
        i = int(v)
        dec = v - i
        if dec == 0:
            v = i
            break
        v *= 10
        multiplier *= 0.1
    multiplier = round(multiplier, 3)

    # break into digits
    digits = []
    while v > 0:
        d = int(v % 10)
        digits.append(d)
        v = int(v / 10)
    digits = deque(reversed(digits))

    # add zeros if not enough digits to meet band requirements,
    # adjusting multiplier as necessary
    while len(digits) < num_digit_bands:
        digits.append(0)
        multiplier *= 0.1
    multiplier = round(multiplier, 3)

    # remove zeros if too many digits for band requirements
    while len(digits) > num_digit_bands:
        d = digits.pop()
        if d != 0:
            raise Exception(f"not enough bands to represent value without losing precision")
        multiplier *= 10
    multiplier = round(multiplier, 3)
    
    # create bands
    bands = []
    for digit in digits:
        bands.append(ResistorValueColor(digit))
    bands.append(ResistorMultiplierColor(multiplier))
    bands.append(ResistorToleranceColor(tolerance))

    return bands
