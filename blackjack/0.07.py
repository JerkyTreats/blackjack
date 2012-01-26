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
        self.hand = []
        self.to_gameplay = []

    #Remove cards from the deck. Player cards, 1 dealer card, return as a list
    def get_hand(self, deck):
        deck = self.deck
        first_card = deck.pop(randint(0, len(deck)-1))
        dealer_card = deck.pop(randint(0, len(deck)-1))
        second_card = deck.pop(randint(0, len(deck)-1))

        self.hand.append(first_card)
        self.hand.append(dealer_card)
        self.hand.append(second_card)
        return self.hand

    #Show the values being dealt to the user. Return a list containing the hand and the deck
    def deal(self, hand, deck_dictionary):
        self.deck_dictionary = deck_dictionary
        self.hand = hand
        
        self.to_gameplay.append(self.hand)
        self.to_gameplay.append(self.deck)
        
        print "Player is dealt: ", self.hand[0]
        print "Dealer is dealt: ", self.hand[1]
        print "Player is dealt: ", self.hand[2]

        return self.to_gameplay

        
class Gameplay(object):
    def __init__(self, deck_dictionary, to_gameplay):
        self.deck_dictionary = deck_dictionary
        self.hand = to_gameplay[0]
        self.deck = to_gameplay[1]
        self.players_total = 0
        
    def Hit(self):
        first_card_value = self.deck_dictionary[self.hand[0]]
        second_card_value = self.deck_dictionary[self.hand[2]]
        self.players_total = self.players_total + (first_card_value + second_card_value)

        if self.players_total == 21:
            print "Sweet Merciful Jesus you got BLACKJACK!"
            return self.players_total

        print "You have: ", self.players_total
        print "\nHIT OR STAY?\n"

        next = raw_input("(Type 'hit' or 'stay' without quotes)\n    > ")

        while self.players_total <= 20:
            if next == 'hit':
                hit_card = self.deck.pop(randint(0, len(deck)-1))
                print "\n You are dealt a ", hit_card
                print hit_card
                hit_card_value = self.deck_dictionary[hit_card]
                self.players_total = (self.players_total + hit_card_value)
                print "You have ", self.players_total
                return self.players_total
            elif next == 'stay':
                return self.players_total
            else:
                print "Incorrect command, please enter 'hit' or 'stay' without quotes"
                #Going to have to think about how to recall the Hit in this else...


    
#-----------------RUNTIME--------------------------------------------------------------------



print "\n\nWELCOME TO BLACKJACK\n\n"

create_deck = Deck()
deck = create_deck.create_deck()
deck_dictionary = create_deck.create_deck_dictionary()


card = Deal(deck, deck_dictionary)
get_hand = card.get_hand(deck)
deal = card.deal(get_hand, deck_dictionary)
game = Gameplay(deck_dictionary, deal)
hit = game.Hit()
