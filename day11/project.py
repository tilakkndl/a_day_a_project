#21 game
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     
print(logo)

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random
cards = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_score = 0
comp_score = 0
keep_playing = False
A_first_occurance_for_user = False
A_first_occurance_for_comp = False
previous_card_for_user=-1
previous_card_for_com=-1
user_card = []
comp_card = []
is_first_chance_palying_user = True
is_first_chance_palying_comp = True

def random_number(staring_num, ending_num):
    return random.randint(staring_num, ending_num)

def calculate_score_user():
    global A_first_occurance_for_user, previous_card_for_user, user_card, is_first_chance_palying_user
    random_nbr = random_number(0, 12)
    # random_nbr = 0
    if random_nbr==0:
        if A_first_occurance_for_user == False and is_first_chance_palying_user == True:
            user_card.append(cards[random_nbr][1])
            is_first_chance_palying_user = False
            A_first_occurance_for_user = True
            previous_card_for_user = -1
        elif A_first_occurance_for_user == False:
            print(cards[random_nbr][1])
            comp_card.append(cards[random_nbr][1])
            A_first_occurance_for_comp = True
            previous_card_for_com = random_nbr
        elif(A_first_occurance_for_user == False and previous_card_for_user != 0):
            user_card.append(cards[random_nbr][0])
            previous_card_for_user = random_nbr
        elif A_first_occurance_for_user == False and previous_card_for_user == 0:
            user_card.pop()
            user_card.append(cards[0][0])
            user_card.append(cards[0][0])
            previous_card_for_user = random_nbr
    else:
        user_card.append(cards[random_nbr])
        previous_card_for_user = random_nbr
    
    return sum(user_card)

def calculate_score_comp():
    global A_first_occurance_for_comp, previous_card_for_com, comp_card, is_first_chance_palying_comp
    random_nbr = random_number(0, 12)
    # random_nbr = 0
    print(f"computer choose: {random_nbr}")
    if random_nbr == 0:
        if A_first_occurance_for_comp == False and is_first_chance_palying_comp == True:
            comp_card.append(cards[random_nbr][1])
            is_first_chance_palying_comp = False
            A_first_occurance_for_comp = True
            previous_card_for_com = -1

        elif A_first_occurance_for_comp == False:
            print(cards[random_nbr][1])
            comp_card.append(cards[random_nbr][1])
            A_first_occurance_for_comp = True
            previous_card_for_com = random_nbr

        elif(A_first_occurance_for_comp == True and previous_card_for_com != 0):
            comp_card.append(cards[random_nbr][0])
            previous_card_for_com = random_nbr

        elif A_first_occurance_for_comp == True and previous_card_for_com == 0:
            comp_card.pop()
            comp_card.append(cards[0][0])
            comp_card.append(cards[0][0])
            previous_card_for_com = random_nbr

    else:
        comp_card.append(cards[random_nbr])
    return (sum(comp_card))

keep_playing = True if input("Do you want to play game? Y or N?").lower()=="y" else False

while(user_score<21 and keep_playing):
    #choose two random cards for user and computer and push to list

    if is_first_chance_palying_user:
        calculate_score_user()
        user_score = calculate_score_user()
        is_first_chance_palying_user = False
        if(user_score==21):
            print("USER won by BLACKJACK")
            calculate_score_comp()
            is_first_chance_palying_comp=False
            comp_score = calculate_score_comp()
            print(f"The computer card is {comp_card}")
            print(f"The computer score is {comp_score}")
            exit()
    else:
        user_score = calculate_score_user()

    print(f"The user cards is {user_card}")
    print(f"User score: {user_score}")
    if is_first_chance_palying_comp:
        comp_score = calculate_score_comp()
        is_first_chance_palying_comp = False
    print(f"The comp cards is {comp_card}")
    print(f"Comp score {comp_score}")
    if(user_score<21):
        keep_playing = True if input("Do you want to add card Y or N?").lower() == "y" else False


while(comp_score<user_score and comp_score<21):
    comp_score = calculate_score_comp()
    print(f"The computer card is {comp_card}")

if(user_score>21):
    print("Computer won USER is PUSHED")
elif(comp_score>21):
     print("waw User won 😄😄😄  COM is PUSHED")
elif(comp_score == user_score):
    print("game is PUSHED")
elif(comp_score>user_score):
    print("Computer won")
else:
    print("waw User won 😄😄😄 ")