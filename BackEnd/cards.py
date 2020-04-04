from typing import Set,List
import random

# Deck and Card classes
SUITS = ("bastoni", "denari", "spade", "coppe")
VALUES = range(1,11)

class Card:
    def __init__(self, suit: str, value: int) -> None:
        self.suit = suit
        self.value = value
        
        # Set points according to value
        if self.value == 8:
            self.points = 2
        elif self.value == 9:
            self.points = 3
        elif self.value == 10:
            self.points = 4
        elif self.value == 3:
            self.points = 10
        elif self.value == 1:
            self.points = 11
        else:
            self.points = 0

    def isBriscola(self, briscolaSuit: str) -> bool:
        return self.suit == briscolaSuit

    def  __gt__(self, other) -> bool:
        if (self.value in [1,3] and other.value in [1,3]):
            return self.value < other.value
        elif (not self.value in [1,3] and other.value in [1,3]):
            return False
        elif (self.value in [1,3] and not other.value in [1,3]):
            return True
        else:
            return self.value > other.value
        

    def prettyPrint(self) -> None:
        print ("{} di {}, punti {}".format(self.value,self.suit,self.points))
    
class Deck:
    def __init__(self) -> None:
        self.cards = []
        # Build deck
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit,value))

    def shuffle(self) -> None:
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self) -> Card:
        return self.cards.pop(0)
    
    def isEmpty(self) -> bool:
        return not self.cards
    
    def prettyPrint(self) -> None:
        for card in self.cards:
            card.prettyPrint()