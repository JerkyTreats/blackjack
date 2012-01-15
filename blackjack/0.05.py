#---------DOC NOTES----------------------------------------------------------------------------------

#CHANGELIST:
#0.02 - 13/01/12 23:17-0:47
#0.03 - 14/01/12 12:50-14:20; 15:00-17:35; 19:30-22:10

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



class Deal(object):
    def __init__(self, deck, deck_dictionary):
        self.deck = deck
        self.card_and_deck = ['null']
        self.hand = []
        self.dealers_card = []
        self.card = "null"

    #What's supposed to happen here is you getting 2 player cards and one dealer card. 
    #For some reason, dealer_card only is returning get_card_and_deck
    def get_hand(self):
        get_first_card = self.get_card_and_deck(self.card, self.deck)
        deck = self.card_or_deck(get_first_card, 'deck')
        first_card = self.card_or_deck(get_first_card, 'card')
        print "this is first_card\n"
        
        get_dealer_card = self.get_card_and_deck(first_card, deck)
        deck = self.card_or_deck(get_dealer_card, 'deck')
        dealer_card = self.card_or_deck(get_dealer_card, 'card')
        print "This is dealer_card\n", dealer_card

        get_second_card = self.get_card_and_deck(dealer_card, deck)        
        deck = self.card_or_deck(get_second_card, 'deck')
        second_card = self.card_or_deck(get_second_card, 'card')
        print "This is second_card\n"

        hand = [first_card, second_card, dealer_card]
        return hand
        

    def get_card_and_deck(self, card, deck):
        deck = self.deck
        card = self.card
        card = deck.pop(randint(0, len(deck)-1))

        del self.card_and_deck[0]
        self.card_and_deck.append(card)
        self.card_and_deck.append(deck)
        return self.card_and_deck
        
    def card_or_deck(self, card_and_deck, switch):
        #print self.card_and_deck[0]
        self.card_and_deck = card_and_deck
        #print self.card_and_deck[0]
        if switch == 'card':
            return self.card_and_deck[0]
        elif switch == 'deck':
            return self.card_and_deck[1]
        else:
            return 'Class: Deal - Func: split - fatal error' 

    def deal(self, hand, deck, deck_dictionary):
        self.deck_dictionary = deck_dictionary
        self.hand = hand
        self.deck = deck
        print "card one: ", self.hand[0]
        print "card two ", self.hand[1]
#        print "card dealer ", self.hand[2]
#        first_card_value = self.deck_dictionary[self.hand[0]]
#        second_card_value = self.deck_dictionary[self.hand[1]]
#        dealer_card_value = self.deck_dictionary[self.hand[2]]
#        print "Player is dealt: ", self.hand[0]
#        print "Dealer is dealt: ", self.hand[2]
#        print "Player is dealt: ", self.hand[1]
#        print "\nPlayers total: ", (first_card_value + second_card_value)   
#        print "\n\n\n", len(deck)   

        

#-----------------RUNTIME--------------------------------------------------------------------



print "\n\nWELCOME TO BLACKJACK\n\n"

create_deck = Deck()
deck = create_deck.create_deck()
deck_dictionary = create_deck.create_deck_dictionary()


card = Deal(deck, deck_dictionary)
get_hand = card.get_hand()
deal = card.deal(get_hand, deck, deck_dictionary)



