from random import randint

BASIC_CARD = 0
HAND_CARD = 1
FLIP_CARD = 2
DOUBLE_CARD = 3

class Card(object):
    """Pazaak Card Class."""

    def __init__(self, cardtype, value: int, sign: str, special: str):
        self.value = value
        self.sign = sign
        self.cardtype = cardtype
        self.special = special
        if self.cardtype == BASIC_CARD or self.cardtype == HAND_CARD:
            self.stringvalue = self.sign + str(self.value)
        else:
            self.stringvalue = self.special

    def __new__(cls, cardtype, value: int, sign: str, special: str):
        if (cardtype == BASIC_CARD and (sign != "+")):
            raise ValueError
        if (cardtype == HAND_CARD
        and ((value < 1 or value > 6) or sign not in ["-","-/+","+","+/-"])):
            raise ValueError
        if (cardtype == FLIP_CARD
        and ((value != 0) or special not in ["2/4","4/2","3/6","6/3"])):
            raise ValueError
        if (cardtype == DOUBLE_CARD and ((value != 0) or special != "double")):
            raise ValueError
        return object.__new__(cls)

    def __str__(self):
        return self.stringvalue

def BuildCard(cardtype, value=None, sign="+", special=""):
    if value is None:
        value = randint(1, 10)
    try:
        newCard = Card(cardtype,value,sign,special)
    except ValueError:
        print(ValueError)
    return newCard

def BuildDeck():
    deck = []
    cards = 0
    while cards < 40:
        newCard = BuildCard(BASIC_CARD)
        nb_card = 0
        for card in deck:
            if card.stringvalue == newCard.stringvalue:
                nb_card += 1
        if nb_card < 4:
            deck.append(newCard)
            cards += 1
    return deck

def BuildHand(cardlist):
    sidedeck = []
    for c in cardlist:
        if c == "double":
            sidedeck.append(BuildCard(DOUBLE_CARD,0,special="double"))
        elif c in ["2/4","4/2","3/6","6/3"]:
            sidedeck.append(BuildCard(FLIP_CARD,0,special=c))
        else:
            sidedeck.append(BuildCard(HAND_CARD,int(c[1]),c[0]))
    return sidedeck

def BuildSideDeck(cardstring):
    cardlist = cardstring.lower().split(";")
    cardlist = [c.strip() for c in cardlist]
    cardlist = [c for c in cardlist if c]
    cardlist = [(c[:-1],c[-1]) if (c.lower() not in ["2/4","4/2","3/6","6/3","double"]) else (c) for c in cardlist]
    hand = BuildHand(cardlist)
    return hand

if __name__ == "__main__":
    deck = BuildDeck()
    print("Deck Builded !")
    sidedeck="   +/-3; +5; -4;-/+2;  ; double;2/4"
    hand = BuildSideDeck(sidedeck)
    print("Hand Builded !")
