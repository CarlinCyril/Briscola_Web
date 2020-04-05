from typing import Set,List
import random

# Card enums
SUITS = ("bastoni", "denari", "spade", "coppe")
VALUES = range(1,11)

class Card:
    """
    Class which represents a card.

    Attributes:
    suit (str): suit of the card.
    value (int): value of the card.
    points (int): how many points the card is worth (in briscola).

    """
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

    def isSuit(self, suit: str) -> bool:
        """
        Given a suit as input, checks whether the card is of that suit or not.

        Args:
            suit: the suit to compare.

        Returns:
            True if the card is of the input suit, False otherwise.
        """
        return self.suit == suit

    def  __gt__(self, other) -> bool:
        """
        Override > operator for Cards: the value is taken into account, following briscola rank (A>3>10>9>8>7>6>5>4>2)

        Returns:
            True if the first card's rank is higher than the seconde one's, False otherwise.
        """
        if (self.value in [1,3] and other.value in [1,3]):
            return self.value < other.value
        elif (not self.value in [1,3] and other.value in [1,3]):
            return False
        elif (self.value in [1,3] and not other.value in [1,3]):
            return True
        else:
            return self.value > other.value
        

    def prettyPrint(self) -> None:
        """
        Method to pretty print the card's attributes.

        Args:
            None.

        Returns:
            None.
        """
        print ("{} di {}, punti {}".format(self.value,self.suit,self.points))
    
class Deck:
    """
    Class which represents a deck of cards.

    Attributes:
    cards (list of Card): list of cards in the deck.

    """
    def __init__(self) -> None:
        self.cards = []
        # Build deck
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit,value))

    def shuffle(self) -> None:
        """
        Method to pretty print the card's attributes.

        Args:
            None.

        Returns:
            None.
        """
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self) -> Card:
        """
        Remove the first card of the deck and return it.

        Args:
            None.

        Returns:
            The card which has been removed.
        """
        return self.cards.pop(0)
    
    def isEmpty(self) -> bool:
        """
        Check if the deck is empty.

        Args:
            None.

        Returns:
            True if there are no more cards in the deck, False otherwise.
        """
        return not self.cards
    
    def prettyPrint(self) -> None:
        """
        Method to pretty print the cards in the deck.

        Args:
            None.

        Returns:
            None.
        """
        for card in self.cards:
            card.prettyPrint()