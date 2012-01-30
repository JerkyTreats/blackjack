#---------IMPORTS-------------------------------------------------------------------------------------



from random import randint
from sys import exit


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
        first_card = deck.pop(randint(0, len(self.deck)-1))
        dealer_card = deck.pop(randint(0, len(self.deck)-1))
        second_card = deck.pop(randint(0, len(self.deck)-1))

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
        self.to_dealer = []
        self.to_win_condition = []

    def Hit(self):
        gamelive = True

        #Get number values from the card, calculate total.
        first_card_value = self.deck_dictionary[self.hand[0]]
        second_card_value = self.deck_dictionary[self.hand[2]]
        self.players_total = self.players_total + (first_card_value + second_card_value)
        self.to_dealer.append(self.players_total)
        self.to_dealer.append(self.deck)
        self.to_dealer.append(self.hand)

        if self.players_total == 21:
            print "Sweet Merciful Jesus you got BLACKJACK!"

        while gamelive == True: 
            if self.players_total == 21:
                print "Nice, you got 21!"
                del self.to_dealer[0]
                self.to_dealer.insert(0, self.players_total)
                gamelive = False

            elif self.players_total <= 20:
                print "You have: ", self.players_total
                print "\nHIT OR STAY?\n"
                next = raw_input("(Type 'hit' or 'stay' without quotes)\n    > ")    

                if next == 'hit':
                    hit_card = self.deck.pop(randint(0, len(self.deck)-1))
                    self.hand.append(hit_card)
                    print "\n You are dealt a ", hit_card
                    hit_card_value = self.deck_dictionary[hit_card]
                    self.players_total = (self.players_total + hit_card_value)

                    del self.to_dealer[0]
                    del self.to_dealer[0]
                    del self.to_dealer[0]
                    self.to_dealer.insert(0, self.players_total)
                    self.to_dealer.insert(1, self.deck)
                    self.to_dealer.insert(2, self.hand)

                    print "You have ", self.players_total

                elif next == 'stay':
                    gamelive = False

                else:
                    print "ERROR: Incorrect command, please enter 'hit' or 'stay' without quotes"
                    pass

            elif self.players_total >= 21:
                print "Bust"
                gamelive = False

        return self.to_dealer

    def DealerPlay(self, to_dealer):
        to_dealer = self.to_dealer
        players_total = to_dealer[0]
        self.deck = to_dealer[1]
        active_cards = to_dealer[2]
        dealers_first_card = active_cards[1]
        dealers_new_cards = []

        dealers_second_card = self.deck.pop(randint(0, len(self.deck)-1))
        first_card_value = self.deck_dictionary[dealers_first_card]
        second_card_value = self.deck_dictionary[dealers_second_card]
        dealers_total = (first_card_value + second_card_value)

        print "Dealer has ", dealers_first_card, " and ", dealers_second_card

        if dealers_total <= 16:
            print "Dealer hits under 17"

            while dealers_total <= 16:
                hit_card = self.deck.pop(randint(0, len(self.deck)-1))
                dealers_total = (dealers_total + self.deck_dictionary[hit_card])
                dealers_new_cards.append(hit_card)

            print "Dealer gets: ", ", ".join(dealers_new_cards)
                        
        self.to_win_condition.append(players_total)
        self.to_win_condition.append(dealers_total)
        return self.to_win_condition


class WinCondition(object): 
    def __init__(self, win_condition):
        self.win_condition = win_condition
        
    def CalculateWinner(self):
        play = Play(False)   

        players_cards = self.win_condition[0]
        dealers_cards = self.win_condition[1]

        print "Players total: ", players_cards
        print "Dealers total: ", dealers_cards
        print "\n\n"

        
        
        if players_cards == 21:
            print "Congratulations, 21 wins!"
            playagain = play.FirstPlay()
        elif dealers_cards >= 22:
            print "Dealer bust, you WIN!"
            playagain = play.FirstPlay()
        elif players_cards == dealers_cards:
            print "Push"
            playagain = play.FirstPlay()            
        elif players_cards >= dealers_cards:
            print "You beat the dealer! You WIN!"
            playagain = play.FirstPlay()
        elif players_cards <= dealers_cards and dealers_cards <= 21:
            print "Lost to the dealer."
            playagain = play.FirstPlay()
        else:
            print "Error = WinCondition: CalculateWinner"

class Play(object):
        def __init__(self, firstplay):
            self.firstplay = firstplay

        def Play(self):
            create_deck = Deck()
            deck = create_deck.create_deck()
            deck_dictionary = create_deck.create_deck_dictionary()


            card = Deal(deck, deck_dictionary)
            get_hand = card.get_hand(deck)
            deal = card.deal(get_hand, deck_dictionary)
            game = Gameplay(deck_dictionary, deal)
            hit = game.Hit()
            dealerplayer = game.DealerPlay(hit)
            wincalc = WinCondition(dealerplayer)
            winner = wincalc.CalculateWinner()

        def FirstPlay(self):

            if self.firstplay == True:
                print "\n\nWELCOME TO BLACKJACK\n\n"
                self.Play()
            elif self.firstplay == False:
                print "\nDo you want to play again?"
            
                next = raw_input("Yes or No: ") 
                print next
                if next == 'no':
                    print "Thanks for playing!"
                    exit(0)
                elif next == 'yes':
                    print next
                    self.Play() 
            else:
                print "Error - Play:FirstPlay"


#-----------------RUNTIME--------------------------------------------------------------------

first_play = Play(True)
play = first_play.FirstPlay()


