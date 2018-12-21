# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 01:18:17 2018

@author: user
"""

def response_ok1(response):
   """ The function returns "True" if the response of the user is either 1 or 2
   and "False" otherwise. This is needed to check the first user responses
   before the actual game starts."""
   while True:
       try:
           int(response)
           break
       except ValueError:
           return False
   response = int(response)
   if response==1 or response==2:
       return True
   else:
       return False

def random_permutation(colours):
   """ This function generates a random permutation. As the Code consists of four
   colours and no repetitions are allowed, there are 6*5*4*3=360 possible codes."""
   index = random.randrange(0, 360)
   i = 0
   for p in itertools.permutations(colours):
        if i == index:
            return p
        i += 1

def all_colours(colours, positions):
    """ This function generates a random permutation."""
    colours = random_permutation(colours)
    for s in itertools.permutations(colours, positions):
        yield s

def check(permutation1, permutation2):
   """ This function calculates the number of rightly_positioned and right_colour
   given two permutations. This is basically what the user does, if he is playing
   the game as codemaker """
   right_positioned = 0
   right_colour = 0
   for i in range(len(permutation1)):
      if permutation1[i] == permutation2[i]:
          right_positioned += 1
      else:
         if permutation1[i] in permutation2:
             right_colour += 1
   return [right_positioned, right_colour]

def inconsistent(new_guess, guesses):
   """ The function checks, if if a permutation new_guess, i.e. a list of 
   colours like new_guess = ["Yellow","Green","Blue","Red"], is consistent
   with the previous colours (i.e. whether new_guess could be the user's code).
   Each previous colour permuation (guess[0] in the list guesses) compared
   with new_guess has to return the same amount of rightly_positioned and
   right_colour as the corresponding evaluation, which was previously given by
   the user (guess[1] in the list "guess"). """
   for guess in guesses:
      res = check(guess[0], new_guess)
      (rightly_positioned, right_colour) = guess[1]
      if res != [rightly_positioned, right_colour]:
         return True # inconsistent
   return False # i.e. consistent

def response_ok2(response):
   """ The function checks the users input for rightly_positioned and right_colour.
   It returns "True" if the response of the user makes sense and "False" otherwise.
   In particular the function checks whether the user entered a number and whether
   the sum of rightly_positioned and right_colour is smaller or equal to 4.
   Furthermore, an input of 3 for rightly_positioned in combination with an input
   of 1 for right_colour doesn't make sense."""
   (rightly_positioned, right_colours) = response
   while True:
       try:
           int(rightly_positioned)
           break
       except ValueError:
           return False
   while True:
       try:
           int(right_colours)
           break
       except ValueError:
           return False
   rightly_positioned = int(rightly_positioned)
   right_colours = int(right_colours)
   if (rightly_positioned + right_colours > 4) or (rightly_positioned + right_colours < len(colours) - 4):
      return False
   if rightly_positioned == 3 and right_colours == 1:
      return False
   return True
  
def view_guesses():
   """ This functions prints the list of all guesses with the corresponding evaluations. """
   print("\nPrevious Guesses (rightly positioned) (right colour)")
   for guess in guesses:
      guessed_colours = guess[0]
      for c in guessed_colours:
         print(c, end=" ")
      for i in guess[1]:
         print(" (%i) " % i, end=" ")
      print()
      
print("Copyright by F & M\n"+"-"*60+"\n"+" "*25,"MASTERMIND\n"+"-"*60,"\n"
      "\nDo you want to know the rules or start the game directly?\n"
      "Rules and explanations -> Enter 1\n"
      "Start the game         -> Enter 2")  
""" The programm asks the user for his input checks it and asks for a new input, if the previous input was invalid."""
s = input()
while response_ok1(s) == False:
    print ("-"*50+"\nInput Error: Enter 1 or 2\n"+"-"*50)  
    s = input()
s=int(s)

""" The Rules and explanations are only shown, if the user enters 1. """
if s == 1:
    print("\nGoal: Codebreaker tries to guess the code of the codemaker in less than 10 rounds!\n"
          "1) Codemaker selects a code consisting of 4 different colours without repetition out of the following:\n"
          "   Yellow, Green, Blue, Red, Pink, White\n"
          "2) The Codebreaker starts guessing the colour code.\n"
          "3) Codemaker gives feedback:\n"
          "   a) How many colours are correct and have the right position. (-> Rightly positioned)\n"
          "   b) How many colours are correct but on the wrong position. (-> Right colours)\n"

          "   Example:\n"
          "   Code: Yellow Blue Green White\n"
          "   Guess: White Blue Green Red\n"
          "   => right positioned: 2 (since Blue and Green are correct and have the right position)\n"
          "   => right colours: 1 (since White is correct but on the wrong position )\n"
          "4) Once Codemaker's feedback is provided, the Codebreaker has to guess the next code depending on the given feedback.\n"
          "5) Again, Codemaker provides feedback on the newly guessed code. (s. 3)\n"
          "This is repeated until the code is guessed or the maximum of ten rounds is reached.\n")
    
print("\nDo you want to be the codemaker?   -> Enter 1\n"
      "Do you want to be the codebreaker? -> Enter 2")
 
""" The programm asks the user for his input, checks it and asks for a new input, if the previous input was invalid. """
s= input()
while response_ok1(s) == False:
    print ("-"*50+"\nInput Error: Enter 1 or 2\n"+"-"*50)  
    s = input()
s=int(s)

import random
import itertools

""" Initializing the game. """         
colours=["Yellow","Green","Blue","Red","Pink","White"]
guesses=[]
round=0
generator=all_colours(colours,4)
a=0
rightly_positioned=0

""" Computer is codebreaker. """
if s==1:
    print ("\nCreate your code consisting of 4 colours without repetition!\nAvailable colours:", end=" ")
    for c in colours:
        print(c, end=" ")
    print ("\n(Its's helpful to write your code down.)")
    input ("If you are ready to start, press enter...")
    while rightly_positioned != 4 and round<10 and a==0:
        """ The programm repeats to generate new guesses for maximal ten rounds, as 
        long as the value of rightly_positioned is smaller than 4
        (if rightly_positioned is equal to 4 the code is solved and the computer won). """
        new_guess=next(generator) # generate a new_guess
        while inconsistent (new_guess, guesses): # As long as the new guess is inconsistent (i.e. it can not be the users code according to the previous evaluations) the computer generates a new guess.
            try:
                new_guess=next(generator)
            except StopIteration: # If there is no possibility to make a consitent new_guess (i.e. there is no code, that can fulfill all the previous evaluations), the program stops and prints an error-message.
                print("*"*50,"\nError: Your answers are inconsistent!\nGAME OVER :-(")
                a=1
                break
        if a==0:
            print("\n"+"*"*50+"\n\nRound:",round+1)
            if round != 0:
                view_guesses()
            print("\nNew Guess:")
            for c in new_guess: # show the new guess to the user
                print(c, end=" ")
            # The programm asks the user for his evaluation, checks it and asks for a new input, if the previous input was invalid.
            rightly_positioned = input("\nRightly positioned: ")
            right_colours = input("Right colours: ")
            while response_ok2([rightly_positioned, right_colours]) == False:
                print ("-"*50,"\nInput Error: Sorry, the input makes no sense!\nTry again!")  
                print ("-"*50,"\nRepeated Guess:")
                for c in new_guess:
                    print(c, end=" ")
                rightly_positioned = (input("\nRightly positioned: "))
                right_colours = (input("Right colours: "))
            rightly_positioned = int(rightly_positioned)
            right_colours = int(right_colours)
            # The new guess as well as the evaluation are added to the list "guesses". This list is then used to check the consistency of the following codes.
            guesses.append((new_guess,(rightly_positioned,right_colours)))
            round = round +1     
    if a==0:
        if round<10:
            print("\n"+"*"*40,"\nComputer won! (Computer was able to crack your code in", round, "rounds)\nGAME OVER")
        else:
            print("You won! (Computer wasn't able to crack your code in 10 rounds)")

""" Computer is codemaker. """            
if s==2:
    print ("\nThe computer generated a code!")
    input ("If you are ready to start, press enter...")
    
    code=next(generator)
    new_guess = []
    
    while rightly_positioned != 4 and round<10:
        """ The programm repeats to evaluate the users guesses for maximal ten rounds,
        as long as the value of rightly_positioned is smaller than 4
        (if rightly_positioned is equal to 4 the code is solved and the user won). """
        print("\n"+"*"*50+"\n\nRound:",round+1)
        print ("Available colours:", end=" ") # show to the user, which colours are available
        for c in colours:
            print(c, end=" ")
        if round != 0:
            print ("\n")    
            view_guesses()
        while new_guess==[]:
            """ The programm asks the user for his new guess, checks it and asks for a new input, if the previous input was invalid. """
            new_guess=list(map(str, input("\nEnter your Guess (capitalized & seperated by space):\n").split(" ")))
            if len(new_guess) != len(set(new_guess)): # Input is invalid if it contains repetitions.
                print("Input error, try again!")
                new_guess=[]
            if len(new_guess)!=4: # Input is invalid if it contains not exactly 4 elements.
                print("Input error, try again!")
                new_guess=[] 
            if not set(new_guess).issubset(colours): # Input is invalid if it contains elements which are not part of the list "colours".
                print("Input error, try again!")
                new_guess=[]              
        """ Valid user input is added to the list "guesses".
        Programm evaluates rightly positioned colours and right colours of users input. The evaluation is also added to the list. """
        guesses.append((new_guess,(check(code, new_guess))))
        rightly_positioned=check(code,new_guess)[0] 
        new_guess=[]
        round=round+1
    if round<10:
        print("*"*40+"\nYou won! (You were able to crack the code in", round, "rounds)")
    else:
        print("*"*40+"\nYComputer won! (You were not able to crack the computer-generated code in 10 rounds)\n"
              "The code was:")
        for c in code:
            print(c, end=" ")
        print ("GAME OVER")