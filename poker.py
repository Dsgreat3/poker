#!/usr/bin/python
# -*- coding: UTF_8 -*-

from enum import Enum
import random

# TODO:
# seat the players at the table etc.
# Nagi's avatar on github
# Testing password management

# Requirements
# Comparison table for pocket cards strength. (for 2-9 players)
# Query: e.g. got 3 cards of one color after flop. What's the probability of a flush., Got three of a kind, how probably can someone has a full house.
# Play of 2-9 players. Each player will get a "brain" (poker strategy algorithm).
# Be able to randomly generate players

# Card names:
# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
class CardValue(Enum):
    ace = 13
    king = 12
    queen = 11
    jack = 10
    ten = 9
    nine = 8
    eight = 7
    seven = 6
    six = 5
    five = 4
    four = 3
    trey = 2
    deuce = 1

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
    def deal(self, player):
        player.giveCard(self.cards.pop())

##Possible Hands
##this class will check what the value of the players hand is
class Hands:
    #variable decliration
    value = 0
    highcard = 0
    NumberOfPairs = 0
       
    ##pass this function all the cards the player has acces to its hand and the river and it will return the value of the hand and the value of the high card
    ##returned values are "ValueOfHand,ValueOfHighCard"  
    def Check (Card0,Card1,Card2,Card3,Card4,Card5,Card6):
        ##converting the input to a list in probely doing it a dumb way not sure how else though - dsgreat
        checkCard = []
        
        for x in range(7):
            checkCard.append([])
        
        #TODO Convert Picture cards values to ints    
        #checkCard[n][0] == the cards value checkCard[n][1] == the cards color        
        checkCard[0].append(Card0()[0])
        checkCard[0].append(Card0()[1])
        checkCard[1].append(Card1()[0])
        checkCard[1].append(Card1()[1])
        checkCard[2].append(Card2()[0])
        checkCard[2].append(Card2()[1])
        checkCard[3].append(Card3()[0])
        checkCard[3].append(Card3()[1])
        checkCard[4].append(Card4()[0])
        checkCard[4].append(Card4()[1])
        checkCard[5].append(Card5()[0])
        checkCard[5].append(Card5()[1])
        checkCard[6].append(Card6()[0])
        checkCard[6].append(Card6()[1])
        
        #curently Card() for card values greater than 10 returns a letter this is change that to a int
        i = 0
        for card in checkCard:
            if (card[0] == "A"):
                checkCard[i][0] = 14
            elif (card[0] == "K"):
                checkCard[i][0] = 13
            elif (card[0] == "Q"):
                checkCard[i][0] = 12
            elif (card[0] == "J"):
                checkCard[i][0] = 11
            elif (card[0] == "T"):
                checkCard[i][0] = 10
            
            checkCard[i][0] = int(checkCard[i][0])            
            i += 1
            
        #find high card
        def highcard (checkCard):
            highcard = 0
            for card in checkCard:
                if (card[0] > highcard):
                    highcard = card[0]
            return highcard
        
        #find pair, three of a kind, full house and four of a kind returns the value of the hand 
        #(pair = 1, 2 pair = 2, 3 of a kind = 3, FullHouse = 6, Four Of A Kind 7)
        #TODO add highcard/Tiebreak
        def similarCards(checkCard):
            cardValues = []
            pairs = []
            threeOfAKind = 0
            FourOfAKind = 0
            Value = 0
            
            for x in range(7):
                cardValues.append(checkCard[x][0])
            
            for x in range(13):
                if (cardValues.count(x) == 2):
                    pairs.append(x)
                elif (cardValues.count(x) == 3):
                    threeOfAKind += 1
                elif (cardValues.count(x) == 4):
                    FourOfAKind += 1   
            if (len(pairs) == 1):
                Value = 1
            if (len(pairs) == 2):
                Value = 2
            if (threeOfAKind == 1):
                Value = 3
            if (len(pairs) == 1 and threeOfAKind == 1):
                Value = 6
            if (threeOfAKind > 1 ):
                Value = 6
            if (FourOfAKind > 0):
                Value = 7
                
            return Value
        
        #returns 4 if their is a stright else returns 0
        def straight(checkCard):
            #sort all the cards values into an list and sort that list
            cardSequncelist = []
            cardSequnce = 0
            comparisonSequncelist = []
            value = 0
            straight = 0
            for card in checkCard:                
                # add the ace to the start of the sqence aswell as the end
                if (card[0] == 13):
                    cardSequncelist.insert(0,0)
                cardSequncelist.append(card[0])
                
            ##remove duplicate cards
            cardSequncelist = list(set(cardSequncelist))
            cardSequncelist.sort()
            
            #make the list a simple sequnce for easy comparison
            for card in cardSequncelist:
                if (cardSequnce == 0):
                    cardSequnce = str(card)
                else:
                    cardSequnce = cardSequnce+str(card)
            
            increment = 0
            
            #create the list to hold the comparision lists
            for x in range(len(cardSequnce)-4):
                comparisonSequncelist.append(0)
            
            #create the comparision lists themselves 
            while increment != (len(cardSequnce)-4):                
                incriment2 = 0
                while incriment2 != 5:
                    if (str(comparisonSequncelist[increment]) == "0"):                
                        comparisonSequncelist[increment] = str(int(cardSequnce[increment])+incriment2)
                    else:
                        comparisonSequncelist[increment] = str(comparisonSequncelist[increment])+str(int(cardSequnce[increment])+incriment2)
                    incriment2 += 1
                increment += 1
            increment = 0
            
            #Compaire
            while increment != (len(cardSequnce)-4):
                if(str(comparisonSequncelist[increment]) == cardSequnce[0+increment:5+increment]):
                    value =  4
                    straight = cardSequnce[0+increment:5+increment]
                increment += 1
            return (value)
        
        #TODO Add highcard tiebreak
        def flush (checkCard):
            cardSequncelist = []
            value = 0
            for Card in checkCard:
                cardSequncelist.append(Card[1])
            
            #check
            if(cardSequncelist.count('S') >= 5 ):
                value = 5
            elif(cardSequncelist.count('H') >= 5 ):
                value = 5
            elif(cardSequncelist.count('D') >= 5 ):
                value = 5
            elif(cardSequncelist.count('C') >= 5 ):
                value = 5
            #elif()
        
            return(value)
        
        #######################################
        #If statment tree to return the hand
        straight = int(straight(checkCard))
        flush = int(flush(checkCard))
        similarCards = int(similarCards(checkCard))
        #check for straight flush
        if (straight != 0 and flush != 0):
            return 8
        elif (similarCards == 7):
            return 7
        elif (similarCards == 6):
            return 6
        elif (flush != 0):
            return 5
        elif (straight != 0):
            return 4
        elif (similarCards == 3):
            return 3
        elif (similarCards == 2):
            return 2
        elif (similarCards == 1):
            return 1
        else:
            return 0
            
    
class Player():
    def __init__(self, playerName, brain):
        self.name = playerName
        self.brain = brain
        self.cards = set()
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
    def whoIsTheButton(self,listOfPlayers):
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
    """All steps of a game (series of Hands) are run by this class"""
    def __init__(self, setOfPlayers, numberOfSeats, numberOfHands):
        # number of players potentially involved in this game
        self.setOfPlayers = setOfPlayers
        # dictionary of seats at the poker table (later used for mapping Players to seat numbers)
        self.seats = dict(map(lambda x: (x + 1, None), range(len(setOfPlayers))))
        self.numberOfHands = numberOfHands
    def mapPlayersToSeats(self):
        # later, we can have a comples players seating function here, for now, we'll just seat them in the order in which they are pulled out of the set
        # we will want this function to check how many empty seats are there before a Hand is played. That many players may join the game for the next hand.
        for (player, seatNumber) in zip(self.setOfPlayers, self.seats.keys()):
            self.seats[seatNumber] = player
    def playHands(self):
        for n in range(self.numberOfHands):
            print("* Checking for empty seats at the table and seating players who want to play.")
            # create a hand
            hand = Hand()
            # play the hand
            hand.playAHand()


####################
## ACTUAL PROGRAM ##
####################

# create a deck of cards
deckOfCards = Deck()

# create players
Bob = Player("Bob", "all")
Bob.giveCard(deckOfCards.H8)
Bob.giveCard(deckOfCards.C8)
Bob.pocketPair()
Bob.suitedCards()
Quinn = Player("Quinn", "all")
Quinn.giveCard(deckOfCards.HT)
Quinn.giveCard(deckOfCards.HJ)
Quinn.pocketPair()
Quinn.suitedCards()

# create a set of players
setOfPlayers = set([Bob, Quinn])

# define the number of seats at the poker table
numberOfSeats = 9

# define the number of hands to be played
numberOfHands = 4

# create game
game = Game(setOfPlayers, numberOfSeats, numberOfHands)

# run the game
#game.playHands()

handscheck = Hands.Check(deckOfCards.H3, deckOfCards.H3, deckOfCards.H4, deckOfCards.H4, deckOfCards.HJ, deckOfCards.HK, deckOfCards.HQ)

print (handscheck)