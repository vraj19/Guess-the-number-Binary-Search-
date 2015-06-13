# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random 
import simplegui
import math

num_range = 100
secret_number = 0
guess_left = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global secret_number
    global guess_left
    
    secret_number = random.randrange(0,num_range)
    
    if num_range == 100:
        guess_left = 7
    elif num_range == 1000:
        guess_left = 10
   
    print "New game ! Range 0 to ",num_range, " Good Luck ! "
    print "Number of remaining guess ",guess_left, "\n"
    pass

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    
    # button that changes the range to [0,100) and starts a new game 
    
    new_game()
    pass

def range1000():
    global num_range
    num_range = 1000
    
    # button that changes the range to [0,1000) and starts a new game     
    
    new_game()
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global guess_left
    global secret_number
    
    won = False 
    
    print "You Guessed : ", guess
    guess_left = guess_left - 1
    print "Number of Guess Remaining",guess_left 
    
    
    if int(guess) == secret_number :
        won = True
    elif int(guess) > secret_number :
        result = "Lower ! "
    else :
        result = "Higher!"

        
    if won :
        print "Correct !  \n "
        new_game()
        return
    elif guess_left == 0 :
        print "Game Over "
        new_game()
        return
    else :
        print result
    pass

# create frame

f=simplegui.create_frame("Game: Guess the Number !", 300,200)
f.set_canvas_background('Red')

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)",range100,100)
f.add_button("Range is [0,1000)",range1000,100)
f.add_input("Enter your Range",input_guess,100)

# call new_game 
new_game()
f.start()
