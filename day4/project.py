#ROCK, SCISSOR AND PAPER 

import random
def check_winner(user, comp):
    if(user == comp):
        return "Noone won"
    elif(user=="R" and comp == "S"):
        return("User won")
    elif(user == "S" and comp == "P"):
        return "user won"
    elif (user == "p" and comp == "R"):
        return ("user won")
    else:
        return("Computer won")

options = ["R", "S", "P"]
user_selection = input("Enter R, S or P")
print("You choose " + user_selection)

comp_selection = random.randint(0, 2)
print("Comp choose: "+ options[comp_selection])

print(check_winner(user_selection, options[comp_selection]))