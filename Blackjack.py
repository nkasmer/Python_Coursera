# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
prompt = ""
d_score = 0
p_score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hand = "" 
        for card in self.cards:
            hand += card.suit + card.rank + " "
        return hand  	

    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        hand_value = 0
        aces_exist = False
        for card in self.cards:
            if card.rank == 'A':
                aces_exist = True 
            hand_value += VALUES[card.rank]
        if not aces_exist:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else: return hand_value
            
    def draw(self, canvas, pos):
        for card in self.cards:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                    [pos[0] * self.cards.index(card) + 74 + CARD_CENTER[0], 
                    pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
        
    def __str__(self):
        deck = ""
        for card in self.cards:
            deck += card.suit + card.rank + " "        
        return deck


#define event handlers for buttons
def deal():
    global in_play, deck, new_player, dealer, d_score, p_score, outcome, prompt
    if in_play:
        outcome = "You lost this round!"
        prompt = "New deal?"
        d_score += 1
        in_play = False
    else:
        deck = Deck()
        deck.shuffle()
        new_player = Hand()
        new_player.add_card(deck.deal_card())
        new_player.add_card(deck.deal_card())
        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        outcome = ""
        prompt = "Hit or stand?"
        in_play = True
    

def hit():
    global in_play, deck, new_player, d_score, p_score, outcome, prompt
    if new_player.get_value() <= 21 and in_play:
        new_player.add_card(deck.deal_card())
        prompt = "Hit or stand?"
    if new_player.get_value() > 21 and in_play:
        d_score += 1
        in_play = False 
        outcome = "You went bust and lose!"
        prompt = "New deal?"
 
       
def stand():
    global deck, new_player, dealer, in_play, d_score, p_score, outcome, prompt
    prompt = "New deal?"
    if in_play:
        while in_play and dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "You win!"
            p_score += 1
            in_play = False
        else:
            if dealer.get_value() >= new_player.get_value():
                outcome = "You lose!"
                d_score += 1
                in_play = False
            else:
                outcome = "You win!"
                p_score += 1
                in_play = False
        
        
   
        
# draw handler    
def draw(canvas):
    global in_play, deck, new_player, dealer, d_score, p_score, outcome
    canvas.draw_text("Blackjack", [74, 100], 40, "Aqua")
    canvas.draw_text("Score", [440, 60], 28, "Orange")
    canvas.draw_text("Dealer  -  Player", [385, 90], 24, "Orange")
    canvas.draw_text(str(d_score) + "   -   " + str(p_score),
                     [415, 135], 40, "Orange")
    dealer.draw(canvas, [100, 200])
    if in_play:
        canvas.draw_image(card_back, [CARD_CENTER[0], CARD_CENTER[1]], CARD_SIZE, 
        [74 + CARD_CENTER[0], 200 + CARD_CENTER[1]], CARD_SIZE)
        canvas.draw_text(prompt, [418, 400], 20, "Black")
    if not in_play:
        canvas.draw_text("Dealer's hand value is " + 
         str(dealer.get_value()) + ".", [190, 170], 20, "Black")
        canvas.draw_text(prompt, [74 + len(outcome)*15.7, 350], 30, "Black")
    canvas.draw_text("Dealer", [74, 170], 26, "Black")
    canvas.draw_text(outcome, [74, 350], 30, "Black")
    new_player.draw(canvas, [100, 430])    
    canvas.draw_text("Player", [74, 400], 26, "Black")
    canvas.draw_text("Yours hand value is " + 
         str(new_player.get_value()) + ".", [190, 400], 20, "Black")
    
    
    
    
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric