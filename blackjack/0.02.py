from random import randint

#First hack - exploring data structure
#0.01 - 13/01/12 

#The class "Deal" not called for now, trying to figure out where my logic should go. 
#Not knowing from the start how I want this system to work is a killer. 
#Need to investigate how to visualize the whole system first, and fill in the details from the outside in. 


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
    def create_deck_dict(self):
        current_string_value = 0
        for value in self.stringvalue:
            for suit in self.suit:
                current_card = value + ' of ' + suit
                self.deck_dict[current_card] = self.realvalue[current_string_value]
            current_string_value += 1
        return self.deck_dict

    #Create values for the deck list. Creates each card of every suit.
    def create_deck(self):
        for value in self.stringvalue:
            for suit in self.suit:
                self.deck.append(value + ' of ' + suit)
        return self.deck



class Create_Hand(object):

    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.cards = [] #empty list of cards in this hand
        self.deck_dict = deck_dict
  
    def create_hand(self):
        create_card = [0, 1] #define list of cards to be created
        for num in create_card: #loop to create 2 cards
            self.cards.append(self.deck.pop(randint(0, len(deck)-1))) #get a random card from deck (first in range to last index in "deck"), add random card to "cards"
            num += 1
        return self.cards

    def total(self, cards): #takes cards and returns the hard values. May change to return cards, not the total. 
        card1 = deck_dict[self.cards[0]] 
        card2 = deck_dict[self.cards[1]]
        total = card1 + card2
        return total

    def update_deck(self):
        return deck


class Deal(object):
    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.deck_dict = deck_dict
        self.players_cards = "null" #need to define empty vars here or get error
        self.dealers_cards = "null"
        
    def deal_player(self):
        player_cards = Create_Hand(deck, deck_dict) #Create_Hand object called in Deal class. 
        self.cards = player_cards.create_hand() #cards = players cards
        print "You are dealt \n" + self.cards[0] + '\n' + self.cards[1]
        print "Your total: ", player_cards.total(self.cards)
        print "There are ", len(player_cards.update_deck()), " cards left in the deck."
        return deck

    def deal_dealer(self, deck):
        
        dealers_cards = Create_Hand(deck, deck_dict)
        self.dealer_cards = dealers_cards.create_hand() #note difference between dealer/dealers
        print "\nDealer is dealt \n", self.dealer_cards[0], "\n", self.cards[1]
        print "Dealers total: ", dealers_cards.total(self.dealer_cards)
        print "There are ", len(dealers_cards.update_deck()), " cards left in the deck."
        return dealers_cards
        
class Game(object):
    def __init__(self, deck, deck_dict):
        self.deck = deck
        self.deck_dict = deck_dict

        self.player_cards = Create_Hand(deck, deck_dict) #Create_Hand object called in Game class. 
        self.cards = self.player_cards.create_hand() #cards = players cards
        self.total = self.player_cards.total(self.cards) #total = cards total
        self.updated_deck = self.player_cards.update_deck() #get updated deck minus cards after dealing

    def deal_user(self):
        print "You are dealt \n" + self.cards[0] + '\n' + self.cards[1]
        print "Your total: ", self.total
        print "There are ", len(self.updated_deck), " cards left in the deck."

    

    #def deal_dealer():
     #   print "The Dealer is dealt " +


#-----------------RUNTIME--------------------------------------------------------------------




#instantiate Deck obj
create_deck = Deck()
deck = create_deck.create_deck()
#print deck
deck_dict = create_deck.create_deck_dict()

#create_hand = Create_Hand(deck, deck_dict)
#cards = create_hand.create_hand()
#print cards
print " " 
deal = Deal(deck, deck_dict)
deal.deal_dealer(deal.deal_player())
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
