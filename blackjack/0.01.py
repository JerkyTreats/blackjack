from random import randint

#First hack - exploring data structure
#0.01 - 13/01/12 

#---------CLASS DEFINITION----------------------------------------------------------------------------


class Deck(object):
    
    def __init__(self):
        #define each suit in a list
        self.suit = [
            "Hearts",
            "Diamonds",
            "Clubs",
            "Spades"
        ]

        #define all cards as strings
        self.stringvalue = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

        #define all card values
        self.realvalue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        #define empty deck dictonary. Deck dictionary allow us to show String but use values during gameplay.
        self.deck_dict = {}

        #define an empty list to be the deck
        self.deck = []

    #Create the values for the dictionary. Creates each card, connects each written value of the card to the real value of the card
    def Create_Deck_Dict(self):
        current_string_value = 0
        for value in self.stringvalue:
            for suit in self.suit:
                current_card = value + ' of ' + suit
                self.deck_dict[current_card] = self.realvalue[current_string_value]
            current_string_value += 1
        return self.deck_dict

    #Create values for the deck list. Creates each card of every suit.
    def Create_Deck(self):
        for value in self.stringvalue:
            for suit in self.suit:
                self.deck.append(value + ' of ' + suit)
        return self.deck



class Create_Hand(object):

    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.cards = [] #empty list of cards in this hand
        self.deck_dict = deck_dict
  
    def Create_Hand(self):
        create_card = [0, 1] #define list of cards to be created
        for num in create_card: #loop to create 2 cards
            self.cards.append(self.deck.pop(randint(0, len(deck)-1))) #get a random card from deck (first in range to last index in "deck"), add random card to "cards"
            num += 1
        return self.cards

    def Total(self, cards): #takes cards and returns the hard values. May change to return cards, not the total. 
        card1 = deck_dict[self.cards[0]] 
        card2 = deck_dict[self.cards[1]]
        total = card1 + card2
        return total

    def Update_Deck(self):
        return deck

class Deal(object):
    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.deck_dict = deck_dict
        self.players_cards = "null" #need to define empty vars here or get error
        self.dealers_cards = "null"
        
    def Deal_Player(self):
        player_cards = Create_Hand(deck, deck_dict) #Create_Hand object called in Deal class. 
        self.cards = player_cards.Create_Hand() #cards = players cards
        print "You are dealt \n" + self.cards[0] + '\n' + self.cards[1]
        print "Your total: ", player_cards.Total(self.cards)
        print "There are ", len(player_cards.Update_Deck()), " cards left in the deck."
        return deck

    def Deal_Dealer(self, deck):
        
        dealers_cards = Create_Hand(deck, deck_dict)
        self.dealer_cards = dealers_cards.Create_Hand() #note difference between dealer/dealers
        print "\nDealer is dealt \n", self.dealer_cards[0], "\n", self.cards[1]
        print "Dealers total: ", dealers_cards.Total(self.dealer_cards)
        print "There are ", len(dealers_cards.Update_Deck()), " cards left in the deck."
        return dealers_cards
        
class Game(object):
    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.deck_dict = deck_dict

        self.player_cards = Create_Hand(deck, deck_dict) #Create_Hand object called in Game class. 
        self.cards = self.player_cards.Create_Hand() #cards = players cards
        self.total = self.player_cards.Total(self.cards) #total = cards total
        self.updated_deck = self.player_cards.Update_Deck() #get updated deck minus cards after dealing

    def DealUser(self):
        print "You are dealt \n" + self.cards[0] + '\n' + self.cards[1]
        print "Your total: ", self.total
        print "There are ", len(self.updated_deck), " cards left in the deck."

    

    #def DealDealer():
     #   print "The Dealer is dealt " +


#-----------------RUNTIME--------------------------------------------------------------------




#instantiate Deck obj
create_deck = Deck()
deck = create_deck.Create_Deck()
#print deck
deck_dict = create_deck.Create_Deck_Dict()

#create_hand = Create_Hand(deck, deck_dict)
#cards = create_hand.Create_Hand()
#print cards
print " " 
deal = Deal(deck, deck_dict)
deal.Deal_Dealer(deal.Deal_Player())
print deck

#-------------------DEBUG STUFF------------------------------------------------------------------

#create_hand = Create_Hand(deck, deck_dict)
#cards = create_hand.Create_Hand()
#print cards
#total = create_hand.Total()
#print total


#deal = Deal(cards, deck_dict)
#total = deal.Total()
#print total
