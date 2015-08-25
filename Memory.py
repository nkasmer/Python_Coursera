# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, exposed, first_card, second_card, state, turns
    state = turns = 0
    label.set_text("Turns = " + str(turns))
    deck1 = deck2 = range(8)
    deck = deck1 + deck2
    random.shuffle(deck)
    exposed = []
    for card in deck:
        exposed.append([card, False])
        
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, first_card, second_card, state, turns
    card = pos[0] // 50
    print "You clicked on card", exposed[card]
    if state == 0:
        first_card = card
        if exposed[card][1] == False:
            exposed[card][1] = True
            state = 1
    elif state == 1:
        second_card = card
        if exposed[card][1] == False:
            exposed[card][1] = True
            turns += 1
            label.set_text("Turns = " + str(turns))
            state = 2
    else:
        if exposed[card][1] == False:
            exposed[card][1] = True
            if exposed[first_card][0] != exposed[second_card][0]: 
                exposed[first_card][1] = exposed[second_card][1] = False
            first_card = card
            state = 1
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    i = -1
    for card in exposed:
        i += 1
        x1 = i * 50 
        x2 = i * 50 + 50
        if card[1] == False:
            canvas.draw_polygon([[x1,0], [x2,0], [x2,100], [x1,100]], 
                1, "Black", "Green")
        else:
            canvas.draw_text(str(card[0]), [i*50 + 13, 68], 40, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric