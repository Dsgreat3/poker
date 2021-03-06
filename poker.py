﻿#!/usr/bin/python
# -*- coding: UTF_8 -*-

from enum import Enum
import random
from lib import rndint # needed for true random shuffle of the deck of cards
import brain as b

# TODO:
# Nagi's avatar on github

# Requirements
# Comparison table for pocket cards strength. (for 2-9 players)
# Query: e.g. got 3 cards of one color after flop. What's the probability of a flush., Got three of a kind, how probably can someone has a full house.
# Play of 2-9 players. Each player will get a "brain" (poker strategy algorithm).
# Be able to randomly generate players

# Card names:
# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
class CardValue(Enum):
    ace = 14
    king = 13
    queen = 12
    jack = 11
    ten = 10
    nine = 9
    eight = 8
    seven = 7
    six = 6
    five = 5
    four = 4
    trey = 3
    deuce = 2

cardNames = dict(zip((CardValue.ace, CardValue.king, CardValue.queen, CardValue.jack, CardValue.ten, CardValue.nine, CardValue.eight, CardValue.seven, CardValue.six, CardValue.five, CardValue.four, CardValue.trey, CardValue.deuce), ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")))

# Color names:
# S = spades, H = hearts, D = diamonds, C = clubs
class CardColor(Enum):
    spades = 4
    hearts = 3
    diamonds = 2
    clubs = 1

cardColors = dict(zip((CardColor.spades, CardColor.hearts, CardColor.diamonds, CardColor.clubs), ("S", "H", "D", "C")))

# Pocket cards:
# AKs = A and K of the same color (s = suited)

class Card():
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __call__(self, parameter="short"):
        if parameter == "short":
            return cardNames[self.value] + cardColors[self.color]
        if parameter == "text":
            return self.value.name + " of " + self.color.name

class Deck:
    def __init__(self):
        self.SA = Card(CardValue.ace, CardColor.spades)
        self.SK = Card(CardValue.king, CardColor.spades)
        self.SQ = Card(CardValue.queen, CardColor.spades)
        self.SJ = Card(CardValue.jack, CardColor.spades)
        self.ST = Card(CardValue.ten, CardColor.spades)
        self.S9 = Card(CardValue.nine, CardColor.spades)
        self.S8 = Card(CardValue.eight, CardColor.spades)
        self.S7 = Card(CardValue.seven, CardColor.spades)
        self.S6 = Card(CardValue.six, CardColor.spades)
        self.S5 = Card(CardValue.five, CardColor.spades)
        self.S4 = Card(CardValue.four, CardColor.spades)
        self.S3 = Card(CardValue.trey, CardColor.spades)
        self.S2 = Card(CardValue.deuce, CardColor.spades)
        self.HA = Card(CardValue.ace, CardColor.hearts)
        self.HK = Card(CardValue.king, CardColor.hearts)
        self.HQ = Card(CardValue.queen, CardColor.hearts)
        self.HJ = Card(CardValue.jack, CardColor.hearts)
        self.HT = Card(CardValue.ten, CardColor.hearts)
        self.H9 = Card(CardValue.nine, CardColor.hearts)
        self.H8 = Card(CardValue.eight, CardColor.hearts)
        self.H7 = Card(CardValue.seven, CardColor.hearts)
        self.H6 = Card(CardValue.six, CardColor.hearts)
        self.H5 = Card(CardValue.five, CardColor.hearts)
        self.H4 = Card(CardValue.four, CardColor.hearts)
        self.H3 = Card(CardValue.trey, CardColor.hearts)
        self.H2 = Card(CardValue.deuce, CardColor.hearts)
        self.DA = Card(CardValue.ace, CardColor.diamonds)
        self.DK = Card(CardValue.king, CardColor.diamonds)
        self.DQ = Card(CardValue.queen, CardColor.diamonds)
        self.DJ = Card(CardValue.jack, CardColor.diamonds)
        self.DT = Card(CardValue.ten, CardColor.diamonds)
        self.D9 = Card(CardValue.nine, CardColor.diamonds)
        self.D8 = Card(CardValue.eight, CardColor.diamonds)
        self.D7 = Card(CardValue.seven, CardColor.diamonds)
        self.D6 = Card(CardValue.six, CardColor.diamonds)
        self.D5 = Card(CardValue.five, CardColor.diamonds)
        self.D4 = Card(CardValue.four, CardColor.diamonds)
        self.D3 = Card(CardValue.trey, CardColor.diamonds)
        self.D2 = Card(CardValue.deuce, CardColor.diamonds)
        self.CA = Card(CardValue.ace, CardColor.clubs)
        self.CK = Card(CardValue.king, CardColor.clubs)
        self.CQ = Card(CardValue.queen, CardColor.clubs)
        self.CJ = Card(CardValue.jack, CardColor.clubs)
        self.CT = Card(CardValue.ten, CardColor.clubs)
        self.C9 = Card(CardValue.nine, CardColor.clubs)
        self.C8 = Card(CardValue.eight, CardColor.clubs)
        self.C7 = Card(CardValue.seven, CardColor.clubs)
        self.C6 = Card(CardValue.six, CardColor.clubs)
        self.C5 = Card(CardValue.five, CardColor.clubs)
        self.C4 = Card(CardValue.four, CardColor.clubs)
        self.C3 = Card(CardValue.trey, CardColor.clubs)
        self.C2 = Card(CardValue.deuce, CardColor.clubs)
        self.cards = list((self.SA, self.SK, self.SQ, self.SJ, self.ST, self.S9, self.S8, self.S7, self.S6, self.S5, self.S4, self.S3, self.S2, self.HA, self.HK, self.HQ, self.HJ, self.HT, self.H9, self.H8, self.H7, self.H6, self.H5, self.H4, self.H3, self.H2, self.DA, self.DK, self.DQ, self.DJ, self.DT, self.D9, self.D8, self.D7, self.D6, self.D5, self.D4, self.D3, self.D2, self.CA, self.CK, self.CQ, self.CJ, self.CT, self.C9, self.C8, self.C7, self.C6, self.C5, self.C4, self.C3, self.C2))
    def __call__(self, parameter="short"):
        listOfCards = list()
        for card in self.cards:
            listOfCards.append(card(parameter))
        return listOfCards
    def shuffl(self, method):
        pass
    def shuffle(self, shufflingSequence):
        # shufflingSequence is a list of shuffling methods, e.g. [wash, riffle, riffle, box, riffle, cut]
        for method in shufflingSequence:
            self.shuffl(self.cards)
    def randomOrgShuffle(self):
        # Seed Random Generator with true Random Value ans shuffle list
        # random.seed(rndint.get(0, len(self.cards), 1).pop())
        # random.shuffle(self.cards)
        # rndint.get function reference: https://code.google.com/p/pyrndorg/source/browse/trunk/rndint.py?r=2
        pass
    def deal(self, player):
        player.giveCard(self.cards.pop())

class Player():
    def __init__(self, playerName, brain, wantsToJoinAGame=True, wantsToLeaveAGame=False):
        self.name = playerName
        self.brain = brain
        self.cards = set()
        self.wantsToJoinAGame = wantsToJoinAGame
        self.wantsToLeaveAGame = wantsToLeaveAGame
    def giveCard(self, card):
            self.cards.add(card)
    def pocketCards(self):
        # this will print the player's cards ordered
        return sorted(self.cards, key = lambda card: (card.value.value, card.color.value), reverse = True)
    def typePocketCards(self, parameter="short"):
        for card in self.pocketCards():
            print(card(parameter))
    def pocketPair(self):
        return self.pocketCards()[0].value == self.pocketCards()[1].value
    def suitedCards(self):
        return self.pocketCards()[0].color == self.pocketCards()[1].color

#next:
# Class Hand(listOfPlayers)

class Hand():
    """All steps of a hand of poker will be run by this class"""
    def __init__(self):
        pass
    def playAHand(self):
        print("**** A NEW HAND STARTS ****")
        print("* Shuffle the cards.")
        print("* Determine who is the button.")
        print("* Place blinds.")
        print("* Deal cards to the players.")
        print("* Pre-flop bet, move money to the pot.")
        print("* Burn one card and uncover the flop.")
        print("* Flop bet, move money to the pot.")
        print("* Burn one card and uncover the turn.")
        print("* Turn bet, move money to the pot.")
        print("* Burn one card and uncover the river.")
        print("* River bet, move money to the pot.")
        print("* Optional showdown.")
        print("* Determine who is the winner.")
        print("* Transfer the pot to the winner.")
        print("* Collect the cards to the deck.")

class Game():
    """Currently it incorporates the rules of Texas Hold'em. We can later have a Rules() class which's instance can be given to either Game() or Dealer() to tell them how the game should be run.
    The game will also have an endGameCondition (as an instance of Condition()) to tell when this game ends.
    Right now this is simplified to a given numberOfHands which are played and then the game is over."""
    def __init__(self, numberOfHands):
        # number of hands is a preliminary construct, until we have implemented the custom endGameConditions properly.
        # until then, the game ends when a certain number of hands have been played.
        self.numberOfHands = numberOfHands

class Dealer():
    """dealer who runs the game of poker (tells whose turn is it), deals the cards to players and manages the pot at a table."""
    def __init__(self, deck):
        self.deck = deck

class Table():
    """A table has a limited number of seats for the players and it holds the community cards, a.k.a. 'the board'.
    It also inherently has a dealer who deals the cards to players and manages the pot."""
    def __init__(self, numberOfSeats, dealer, game, setOfPlayers):
        self.numberOfSeats = numberOfSeats
        self.dealer = dealer
        self.game = game
        # dictionary of seats at the poker table (later used for mapping Players to seat numbers)
        self.seats = dict(map(lambda x: (x + 1, None), range(numberOfSeats)))
        self.setOfPlayers = setOfPlayers
    def invitePlayers(self):
        """This function maps players who want to join a game to a free seat at the table."""
        # This wil check how many empty seats are there before a Hand is played. That many players may join the game for the next hand.
        setOfEmptySeats = set()
        for seatNumber, player in self.seats.items():
            if player is None:
                setOfEmptySeats.add(seatNumber)
        # from the set of all players we make a list of players who want to join a game.
        listOfPlayersToJoinAGame = list()
        for player in self.setOfPlayers:
            if player.wantsToJoinAGame:
                listOfPlayersToJoinAGame.append(player)
        print("**", len(listOfPlayersToJoinAGame), "players want to join a game")
        # since we want the players to be seated at the table randomly, we will shuffle this list
        random.shuffle(listOfPlayersToJoinAGame)
        for (player, seatNumber) in zip(listOfPlayersToJoinAGame, setOfEmptySeats):
            self.seats[seatNumber] = player
            # Once a player has joined a game, he no longer wants to join one.
            player.wantsToJoinAGame = False
            print("***", player.name, "takes seat", seatNumber)
    def letPlayersGo(self):
        # Until players get more sophisticated brains, they decide randomly whether they want to leave the table or not.
        for seatNumber, player in self.seats.items():
            # We have to check whether a player is sitting at this seat
            if player is not None:
            # let the player decide whether he wants to leave the table
                player.brain.wantToLeaveTheTable = player.brain.tossACoin()
                if player.brain.wantToLeaveTheTable:
                    self.seats[seatNumber] = None
                    print("***", player.name, "has vacated seat", seatNumber)
    def playerList(self):
        """This returns the list of players currently sitting at the table and playing"""
        listOfPlayersPlayingAtTheTable = list()
        for seatNumber, player in self.seats.items():
            if player is not None:
                listOfPlayersPlayingAtTheTable.append(player)
        return listOfPlayersPlayingAtTheTable
    def playGame(self):
        print("* A game is played.")
        for hand in range(self.game.numberOfHands):
            # Check for empty seats at the table and seat the players.
            print("** Checking whether any players want to join the game.")
            self.invitePlayers()
            # create a hand
            hand = Hand()
            # Check whether there are enough players to play poker (at least 2)
            if len(self.playerList()) > 1:
                # play the hand
                print("**", len(self.playerList()), "players play a hand.")
                hand.playAHand()
                print("** Checking whether any players want to leave the game.")
                self.letPlayersGo()
            # otherwise the last remaining player will leave the table. (This mustn't be elif!)
            if len(self.playerList()) == 1:
                # we will tell his brain that he wants to leave the table
                self.playerList()[0].brain.wantToLeaveTheTable = True
                print("** Last remaining player left the table.")
                self.letPlayersGo()
            # otherwise the game is over (This mustn't be elif!)
            if len(self.playerList()) == 0: 
                break
        print("* The game is over and all players have left the table.")

####################
## ACTUAL PROGRAM ##
####################

# create a deck of cards
deckOfCards = Deck()

# create a dealer and give him the deck of cards.
dealer = Dealer(deckOfCards)

# create a set of players interested in a game of poker at a particular table
setOfPlayers = set()

# create players
setOfPlayerNames = set(["Bob", "Quinn", "Jeff", "Lewis", "Sven", "John", "Mary", "Marc", "Gary", "Marlana", "Blanch", "Cathey", "Bruno", "Violeta", "Barton", "Fran", "Hubert", "Barbara", "Nydia", "Cinda", "Enid", "Dalton", "Shae", "Verda", "Tomas", "Terina", "Robin", "Pricilla", "Melba", "Suzan", "Johna", "Shawanda", "Rema", "Madeleine", "Sherilyn", "Lyndsay", "Sau", "Monserrate", "Denice", "Ramonita", "Kenyetta", "Cara", "Caryl", "Olga", "Rosenda", "Lorene", "Kellie", "Myrl", "Carleen", "Porter", "Laurine", "Lucila", "Felisha", "Candace", "Dagny", "Temple", "Lacey", "Estela", "Alexis"])
for name in setOfPlayerNames:
    setOfPlayers.add(Player(name, b.allIn()))

# define the number of hands to be played
numberOfHands = 20000

# create game
game = Game(numberOfHands)

# define the number of seats at the poker table
numberOfSeats = 9

# create a table
table = Table(numberOfSeats, dealer, game, setOfPlayers)

# run the game
table.playGame()

