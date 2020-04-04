# Briscola game class
import uuid
import random
from itertools import tee,islice
from players import Player, Team
from cards import Card, Deck


class Game:

    deck = Deck()

    def __init__(self, player: Player, numPlayers: int) -> None:
        # Game is initialized when 1 player joins
        #Generate unique id for game
        self.id = uuid.uuid1().hex
        self.isFull = False
        self.numPlayers = numPlayers
        firstTeam = Team(player)
        # Team index in the array will be used as its id
        self.teams = [firstTeam]
        # Player order in array is turn order
        self.players = [player]
        self.briscola = None
        self.currentPlayer = None
        # Table is a list of (PlayerIndex,Card) tuples
        self.table = []

    def addPlayer(self, player: Player) -> None:
        if (not self.isFull):
            if (self.numPlayers == 2):
                secondTeam = Team(player)
                self.teams.append(secondTeam)
                self.players.append(player)
                self.isFull = True
            #TODO: add elif for 3,4 and 5 players
        else:
            print("Cannot add player, game is full!")
        

    def startGame(self) -> None:
        self.deck.shuffle()
        # Draw briscola and set it as the last card of the deck
        briscolaCard = self.deck.drawCard()
        self.briscola = briscolaCard.suit
        self.deck.cards.append(briscolaCard)
        #Choose random player to start
        #TODO: add handling for >2 players
        starterPlayerIndex = random.randint(0,self.numPlayers)
        self.currentPlayer = self.players[starterPlayerIndex]
        # Deal initial cards (3)
        #TODO: diff nr of cards for 5 players
        self.dealCards(starterPlayerIndex, 3, self.numPlayers)

    def dealCards(self, firstPlayer:int, numCards: int, numPlayers: int) -> None:
        for i in range(numCards * numPlayers):
            self.players[(i + firstPlayer)%numPlayers].addCardToHand(self.deck.drawCard())

class Hand:
    def __init__(self, firstCard: Card, playerIndex: int, briscola: str):
        self.leadSuit = firstCard.suit
        self.briscolaSuit = briscola
        cardTuple = (playerIndex, firstCard)
        self.table = [cardTuple]
        self.winner = cardTuple
    
    def addCard(self,card: Card, playerIndex : int) -> None:
        cardTuple = (playerIndex, card)
        self.table.append(cardTuple)
        #Determine winner
    
    def isNewWinner(self, previousWinner: Card, newCard: Card) -> bool:
        if (not previousWinner.isBriscola(self.briscolaSuit) and newCard.isBriscola(self.briscolaSuit)):
            return True
        elif (previousWinner.isBriscola(self.briscolaSuit) and not newCard.isBriscola(self.briscolaSuit)):
            return False
        elif (previousWinner.isBriscola(self.briscolaSuit) and newCard.isBriscola(self.briscolaSuit)):
            return newCard > previousWinner
        else:
            if(previousWinner.suit == self.leadSuit and newCard.suit == self.leadSuit):
                return newCard > previousWinner
            elif (previousWinner.suit == self.leadSuit and not newCard.suit == self.leadSuit):
                return False
            elif (not previousWinner.suit == self.leadSuit and newCard.suit == self.leadSuit):
                return True
            else:
                print("Both cards are not briscola nor lead suit - impossible!")
                return False




