###############################################################################
#                         IMPORTS                                             #
###############################################################################

from random import shuffle

###############################################################################
#                         CONSTANTS                                           #
###############################################################################

HAND_CARDS = {
    # Basic Cards
    "-1": ("-","1"),        "+1": ("+","1"),
    "+/-1": ("+/-","1"),    "-/+1": ("-/+","1"),
    "-2": ("-","2"),        "+2": ("+","2"),
    "+/-2": ("+/-","2"),    "-/+2": ("-/+","2"),
    "-3": ("-","3"),        "+3": ("+","3"),
    "+/-3": ("+/-","3"),    "-/+3": ("-/+","3"),
    "-4": ("-","4"),        "+4": ("+","4"),
    "+/-4": ("+/-","4"),    "-/+4": ("-/+","4"),
    "-5": ("-","5"),        "+5": ("+","5"),
    "+/-5": ("+/-","5"),    "-/+5": ("-/+","5"),
    "-6": ("-","6"),        "+6": ("+","6"),
    "+/-6": ("+/-","6"),    "-/+6": ("-/+","6"),

    # Flip Cards & Double
    "2/4": ("f","2/4"),     "4/2": ("f","4/2"),
    "3/6": ("f","3/6"),     "6/3": ("f","6/3"),
    "x2": ("x","2"),
}

SIGN = ["-","-/+","+","+/-","x","f"]

DEFAULT_DECK_SIZE = 40

###############################################################################
#                         CLASSES                                             #
###############################################################################

class Card(object):
    """Pazaak Card Class."""

    def __init__(self, value):
        self.value = value
        self.stringvalue = str(self.value)

    def __new__(cls, value):
        if int(value) < 1 or int(value) > 10: raise ValueError("Invalid Card Value.")
        return object.__new__(cls)

    def __str__(self):
        return str(self.value)


class HandCard(object):
    """Pazaak Hand Card Class."""

    def __init__(self, sign, value):
        self.sign = sign
        self.value = value
        self.stringvalue = self.sign + str(self.value)

    def __new__(cls, sign, value):
        if sign is not None and sign not in SIGN: raise ValueError(f"Invalid Card Sign {sign}.")
        accepted_values = []
        for k,v in HAND_CARDS.items():
            accepted_values.append(v[1])
        accepted_values = list(dict.fromkeys(accepted_values))
        if value not in accepted_values: raise ValueError(f"Invalid Card Value {value}.")
        return object.__new__(cls)

    def __str__(self):
        return self.stringvalue


class Deck(object):
    """Pazaak Deck Class."""

    def __init__(self, cards_qty=DEFAULT_DECK_SIZE, cardlist=None):
        if cards_qty is None or cards_qty <= 0: raise ValueError("Invalid number of Cards.")
        if cardlist is not None and len(cardlist) != cards_qty:
            raise ValueError("The number of cards does not match the number of Cards from the card list.")

        self.cards = []

        # Create a Dealer Deck
        value = 0
        while cards_qty > 0:
            if cardlist is None:
                if cards_qty % 4 == 0:
                    value += 1
                self.cards.append(Card(value))
            # Create a Side Deck or a Hand
            elif cardlist is not None:
                    self.cards.append(HandCard(cardlist[cards_qty-1][0], cardlist[cards_qty-1][1]))
            cards_qty -= 1

        # Shuffle the Deck
        shuffle(self.cards)

        self.stringvalue = ""
        for c in self.cards:
            self.stringvalue += c.stringvalue + ";"

    def __str__(self):
        return self.stringvalue.strip()

###############################################################################
#                         FUNCTIONS                                           #
###############################################################################

def sanitizeCardlist(cardstring):
    cardlist = cardstring.lower().split(";")
    cardlist = [c.strip() for c in cardlist]
    cardlist = [c for c in cardlist if c]
    cleaned = []
    for c in cardlist:
        if c not in HAND_CARDS.keys():
            raise ValueError(f"Invalid card: {c}.")
        else:
            cleaned.append(HAND_CARDS[c])
    return cleaned

if __name__ == "__main__":
    deck = Deck()
    sidedeck_string = "+6;-6;+/-6;-/+6;2/4; x2;4/2 ;  +1  ; -1 ; +/-2"
    cardlist = sanitizeCardlist(sidedeck_string)
    sidedeck = Deck(10,cardlist)
    print(sidedeck)
