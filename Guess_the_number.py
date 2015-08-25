# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math


num_range = 100

# helper function to start and restart the game

def new_game():
    
    # initialize global variables used in your code here
    global secret_number, num_range, rem_guesses
    secret_number = random.randrange(0, num_range)
    rem_guesses = int(math.ceil(math.log(num_range + 1, 2)))
    print "New Game. Range is from 0 to", num_range  
    print "Number of remaining guesses is", rem_guesses


# define event handlers for control panel

def range100():
    
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    print
    new_game()
    

def range1000():
    
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    print
    new_game()
    
    
def input_guess(guess):
    
    # main game logic goes here
    global secret_number, rem_guesses
    inp = int(guess)
    print "\nGuess was", inp
    rem_guesses -= 1
    print "Number of remaining guesses is", rem_guesses
    if rem_guesses > 0:
        if secret_number > inp:
            print "Higher!"
        elif secret_number < inp:
            print "Lower!"
        else:
            print "Correct!\n"
            new_game()
    else:
        if secret_number == inp:
            print "Correct!\n"
        else:
            print "You ran out of guesses! The number was", secret_number, "\n"
        new_game()
   

    
# create frame

f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game 

new_game()


# always remember to check your completed program against the grading rubric

f.start()