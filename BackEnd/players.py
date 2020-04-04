# Player and Team classes
import sys
from cards import Card

class Player:

    def __init__(self, username: str) -> None:
        self.username = username
        self.hand = []

    def playCard(self, cardIndex: int) -> Card:
        return (self, self.hand.pop(cardIndex))

    def addCardToHand(self, card: Card) -> None:
        self.hand.append(card)

class Team:

    def __init__(self, firstMember: Player) -> None:
        self.players = [firstMember]
        self.score = 0

    def addPlayer(self,player: Player) -> None:
        self.players.append(player)
    
    def updateScore(self, points: int) -> None:
        self.score += points