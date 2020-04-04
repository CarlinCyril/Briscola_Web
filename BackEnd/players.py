# Player and Team classes
import sys
from cards import Card

class Player:

    """
    Class which represents a player in a game.

    Attributes:
    username (str): username of the player.
    hand (list of Card): list of the cards which are currently in the player's hand.

    """

    def __init__(self, username: str) -> None:
        self.username = username
        self.hand = []

    def playCard(self, cardIndex: int) -> Card:
        """Given the index of a card, removes it from the player's hand and returns it.

        Args:
            cardIndex: index (in the hand) of the card to be removed and returned.

        Returns:
            The card which has been removed.

        """
        return (self, self.hand.pop(cardIndex))

    def addCardToHand(self, card: Card) -> None:
        """ Adds a card to the player's hand.

        Args:
            card: Card to be added.

        Returns:
            None.

        """
        self.hand.append(card)

class Team:

    """
    Class which represents a team of players in a game.

    Attributes:
    players (list of Player): list of the players in the team.
    score (int): current score of the team.

    """

    def __init__(self, firstMember: Player) -> None:
        self.players = [firstMember]
        self.score = 0

    def addPlayer(self,player: Player) -> None:
        """ Adds a player to the team.

        Args:
            player: Player to be added to the team.

        Returns:
            None.

        """
        self.players.append(player)
    
    def updateScore(self, points: int) -> None:
        """ Given a number of points, updates the score of the team by adding them to the current score.

        Args:
            points: Points to be added to the current score.

        Returns:
            None.

        """
        self.score += points