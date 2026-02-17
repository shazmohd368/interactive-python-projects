# Guess the number mini project

import simplegui
# Note: Uses simplegui from CodeSkulptor (educational environment).

import random


range = 100
guess="None"
guess_count = 7


#Helper function
def new_game():
    
    
    ''' Helper function to start & restart the game'''
    
    
    global secret_number
    global guess_count
    
        
        
    if range ==1000:
        
        guess_count=10
        
        print ""
        print "New game. Range[0-1000)"
        print "Number of remaining guesses is "+str(guess_count)
      
        
        secret_number= random.randrange(0,1000)
        
        
    else:
        
        guess_count=7  
        
        print ""
        print "New game. Range[0-100)"
        print "Number of remaining guesses is "+str(guess_count)
        
        
        secret_number= random.randrange(0,100)
        
        
    
  
# define event handlers 
def range100():
    
    ''' button that changes the range to [0,100) and starts a new game''' 
     

    global range
    
    range =100
    
    new_game()

    
def range1000():
    
    '''button that changes the range to [0,1000) and starts a new game'''  
    global range
    
    
    range =1000
    
    
    new_game()
    
    
def input_guess(guess):
    
    ''' Game's main logic'''
    global guess_count
    
    
    print ""
    print "Your guess was " + str(guess)
    
   
            
    if guess_count == 1 and guess != secret_number :
        
        guess_count=guess_count-1
        
        print "Number of remaining guesses is "+str(guess_count)
        print "Correct answer is "+str(secret_number)
        
        new_game()
        
        
        
    else:
        
        
        if int(guess) == secret_number:
            
            guess_count = guess_count-1
        
            print "Number of remaining guesses is "+str(guess_count)
            print "Correct!"
            
            new_game()
        
        elif int(guess) < secret_number:
            
            guess_count = guess_count-1
            
            print "Number of remaining guesses is "+str(guess_count)
            print "Higher"
        
        else:
            
            guess_count = guess_count-1
            
            print "Number of remaining guesses is "+str(guess_count)
            print "Lower"


    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_input("Guess the number",input_guess, 200)
frame.add_button('New Game',new_game)
frame.add_button('Reset',new_game)
frame.add_button('Range [0-100)',range100)
frame.add_button('Range [0-1000)',range1000)

frame.start()


# call new_game 
new_game()


