"""
Lab4_LanceTho-2.py
Lance Thongsavanh
Write a program where the player tries to guess a random number between 1 and 15.  Each incorrect guess reveals another part of a hangman drawing.
2/3/2026
"""

#import random
import random

#Create a random number, 1 to 15
hangman_value: int = random.randint(1, 15)

#Create a list of triple quoted strings
hangman_drawing: list = [
    """
    ______
    |    |
    |
    |
    |
    |
    ==========
    """,
    """
    ______
    |    |
    |    0
    |
    |
    |
    ==========
    """,
    """
    ______
    |    |
    |    0
    |    |
    |
    |
    ==========
    """,
    """
    ______
    |    |
    |    0
    |    |/
    |
    |
    ==========
    """,
    """
    ______
    |    |
    |    0
    |   \|/
    |
    |
    ==========
    """,
    """
    ______
    |    |
    |    0
    |   \|/
    |   /
    |
    ==========
    """,
    """
    ______
    |    |
    |    0
    |   \|/
    |   / \\
    |
    ==========
    """
    ]

#Create a variable to keep track of the wrong guesses, initialize to 0

#Create a variable to keep track of Game Over [“yes” or “no”]



#Ask the user for a guess

#While the guess is not None:

           

#If guess equal to generated number:

   #Print a congratulations

   #Break out of while loop

#Else:

#Print the next object in the hanged man list

#Increment the wrong guesses

           

#If wrong guesses is equal to length of hanged man list:

#Print a sad message

#Break out of while loop



#Ask user for another guess

