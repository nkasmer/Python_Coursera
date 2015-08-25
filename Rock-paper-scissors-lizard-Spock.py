# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name=='rock':
        result=0
    elif name=='Spock':
        result=1
    elif name=='paper':
        result=2
    elif name=='lizard':
        result=3
    elif name=='scissors':
        result=4
    else:
        print "You gave a wrong name. Please try again!"
    return result



def number_to_name(number):
    if number==0:
        result='rock'
    elif number==1:
        result='Spock'
    elif number==2:
        result='paper'
    elif number==3:
        result='lizard'
    elif number==4:
        result='scissors'
    else:
        print "You gave a wrong number. Please try again!"
    return result
    
    

def rpsls(player_choice): 
    print
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    diff=(comp_number-player_number)%5
    if diff==1 or diff==2:
        print "Computer wins!"
    elif diff==3 or diff==4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
 
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


