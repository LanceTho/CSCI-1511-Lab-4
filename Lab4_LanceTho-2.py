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
wrong_guesses: int = 0

#Create a variable to iterate through the hangman_drawing list
drawing: int = 0


#Ask the user for a guess
print(hangman_drawing[0])
print("Guess a number")
user_guess: int = int(input())

#While the guess is not None:
while user_guess != None:
           

    #If guess equal to generated number:
    if user_guess == hangman_value:

        #Print a congratulations
        print("Congratulations! You guessed the right number!")
        #Break out of while loop
        break

    #Else:
    else:

        #Print the next object in the hanged man list
        print(hangman_drawing[drawing])
        drawing = drawing + 1
        wrong_guesses = wrong_guesses + 1
        #Increment the wrong guesses

           

    #If wrong guesses is equal to length of hanged man list:
    if wrong_guesses == len(hangman_drawing):
        #Print a sad message
        print("Too Bad! You Lose!")
        #Break out of while loop
        break


    if user_guess > hangman_value:
        print("That's too high")

    if user_guess < hangman_value:
        print("That's too low")

    #Ask user for another guess
    print("Guess a number")
    user_guess = int(input())