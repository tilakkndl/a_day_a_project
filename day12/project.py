logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

import random

def guess_message(guessed_nbr, acutal_nbr):
    difference = guessed_nbr-acutal_nbr
    if(difference >= 5):
        return "Too high"
    elif (difference <5 and difference>0):
        return "High"
    elif difference == 0:
        return 1
    elif difference<= -5:
        return "Too low"
    else:
        return "Low"

def generate_random_number ():
    return random.randint(0, 99)

no_of_option = 0
correct_guess = False
correct_number = generate_random_number()
print(f"Correct number = {correct_number}")
guess_number = -1
print("Welcome to the number guessing game: ")
no_of_option = 5 if input("Enter the level you want to play: 'noraml' or 'difficult' ") == "difficult" else 10
print(f"NO of option {no_of_option}")

while(no_of_option != 0 and not correct_guess):
    guess_number = int(input("Guess a number: "))
    return_message = guess_message(guess_number, correct_number)
    if type(no_of_option) == type(return_message):
        correct_guess = True
    else:
        print(return_message)
        no_of_option-=1


if(correct_guess == True):
    print("Congratulations You correctly guessed the number")
elif no_of_option == 0:
    print("You loose a game: ")
