# Briscola game class
import uuid
import random
from itertools import tee,islice
from players import Player, Team
from cards import Card, Deck


class Game:

    """
    Core class used to represent a game of Briscola.

    Attributes:
    deck (Deck): the deck of cards for the game.
    id (str): unique id for the game (32-character hexadecimal string).
    isFull (bool): True if the number of players of the game has been reached.
    numPlayers (int): number of players of the game (can be 2,3,4 or 5).
    teams (list of Team): list of the teams in the game (can be 2 or 3).
    players (list of Player): list of all the players in the game.
    briscola (str): briscola suit for the game.
    currentPlayer (Player): the player whose turn it is currently.
    currentDeal (Deal): the current Deal which is being played.

    """

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
        self.currentDeal = None

    def addPlayer(self, player: Player) -> bool:
        """ Adds a player to the game (if it is not full) and assigns it to a team

        Args:
            player: The player to add to the game.

        Returns:
            True if player has been added, False otherwise.

        """
        if (not self.isFull):
            if (self.numPlayers == 2):
                secondTeam = Team(player)
                self.teams.append(secondTeam)
                self.players.append(player)
                self.isFull = True
                return True
            #TODO: add elif for 3,4 and 5 players
        else:
            print("Cannot add player, game is full!")
            return False
        

    def startGame(self) -> None:
        """ Starts the game of briscola (shuffle deck and deal cards).

        Args:
            None.

        Returns:
            None.

        """
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
        """ Deals cards to each player.

        Args:
            firstPlayer: the cards will be dealt starting by the player with this index.
            numCards: the number of cards to be dealt.
            numPlayers: the number of Players in the game.

        Returns:
            None.
            
        """
        for i in range(numCards * numPlayers):
            self.players[(i + firstPlayer)%numPlayers].addCardToHand(self.deck.drawCard())

class Deal:

    """
    A class used to represent a deal - the play from the time the cards are dealt until they are redealt.

    Attributes:
    leadSuit (str): lead suit of the deal (suit of the first played card)
    briscolaSuit (str): briscola suit for the game
    table (list of (int, Card)): list of the cards which are on the table, represented by tuples containing the card and the ID
        of the player who played it
    winner((int,Card)): tuple of the card who is currently winning the deal (is updated everytime card is added to the table)

    """

    def __init__(self, firstCard: Card, playerIndex: int, briscola: str):
        self.leadSuit = firstCard.suit
        self.briscolaSuit = briscola
        cardTuple = (playerIndex, firstCard)
        self.table = [cardTuple]
        self.winner = cardTuple
    
    def addCard(self,card: Card, playerIndex : int) -> None:
        """ Adds a card to the table, and updates the deal's winner accordingly

        Args:
            card: The card to add to the table.
            playerIndex: The id (index) of the player who played the card.

        Returns:
            None.

        """
        cardTuple = (playerIndex, card)
        self.table.append(cardTuple)
        # If the new card wins over the current winner, update the winner
        if (self.isNewWinner(card)):
            self.winner = cardTuple
    
    def isNewWinner(self, newCard: Card) -> bool:
        """ Checks if a card wins over the current card winning the deal.

        Args:
            newCard: The card to compare against the current winning card.

        Returns:
            True if the card wins over the current winning card, False otherwise.

        """
        currentWinner = self.winner[1]
        if (not currentWinner.isSuit(self.briscolaSuit) and newCard.isSuit(self.briscolaSuit)):
            return True
        elif (currentWinner.isSuit(self.briscolaSuit) and not newCard.isSuit(self.briscolaSuit)):
            return False
        elif (currentWinner.isSuit(self.briscolaSuit) and newCard.isSuit(self.briscolaSuit)):
            return newCard > currentWinner
        else:
            if(currentWinner.suit == self.leadSuit and newCard.suit == self.leadSuit):
                return newCard > currentWinner
            elif (currentWinner.isSuit(self.leadSuit) and not newCard.isSuit(self.leadSuit)):
                return False
            elif (not currentWinner.isSuit(self.leadSuit) and newCard.isSuit(self.leadSuit)):
                return True
            else:
                print("Both cards are not briscola nor lead suit - impossible!")
                return False




