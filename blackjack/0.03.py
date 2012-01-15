#---------DOC NOTES----------------------------------------------------------------------------------

#CHANGELIST:
#0.02 - 13/01/12 23:17-0:47
#0.03 - 14/01/12 12:50-

#NOTES:
#V3, major refactor, gutted crappy code as I better understand how I want the system to work
#

#---------IMPORTS-------------------------------------------------------------------------------------



from random import randint



#---------CLASS DEFINITION----------------------------------------------------------------------------



class Deck(object):
    def __init__(self):
        self.suit = [
            "Hearts",
            "Diamonds",
            "Clubs",
            "Spades"
        ]
        self.stringvalue = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        self.realvalue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.deck_dictionary = {}
        self.deck = []

    #Link stringvalues to realvalues into deck_dictionary. 
    def create_deck_dictionary(self):
        current_string_value = 0
        for value in self.stringvalue:
            for suit in self.suit:
                current_card = value + ' of ' + suit
                self.deck_dictionary[current_card] = self.realvalue[current_string_value]
            current_string_value += 1
        return self.deck_dictionary

    #Create values for the deck list. Creates each card of every suit.
    def create_deck(self):
        for value in self.stringvalue:
            for suit in self.suit:
                self.deck.append(value + ' of ' + suit)
        return self.deck



class Player(object):
    def __init__(self, deck):
        self.hand = []
        self.deck = deck
        
    def get_hand(self, card_in):
        player_hand = self.hand.append(card_in)
        return player_hand

    def hit(self, player_hand, deck):
        player_hand = self.player_hand



class Deal(object):
    def __init__(self, deck, deck_dictionary):
        self.deck = deck

    def deal_player(self):
        player_hand = Player(deck)
        player_hand.get_hand(self.deck.pop(randint(0, len(deck)-1)))
        return player_hand


#-----------------RUNTIME--------------------------------------------------------------------



create_deck = Deck()
deck = create_deck.create_deck()
deck_dictionary = create_deck.create_deck_dictionary()

print "BLACKJACK" 
deal = Deal(deck, deck_dictionary)
deal.deal_player()
print deal
