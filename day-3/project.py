#Treasure finding game

print("Welcome to the Treasure finding game")
print("YOur objective is to find the treasure")
print("Your option is 'left' or 'right'")
option = input("Enter a option").lower()
if(option == 'right'):
    print("YOu lose. The game is over")
    exit()
else:
    option = input("Your option is 'swim' or 'wait'").lower()
    if option=="swim":
        print("You lose game")
        exit()
    else:
        option = input("Which door you want to choose: 'red', 'yellow' or 'blue'").lower()
        if(option=="yellow"):
            print("You won")
        else:
            print("You loose")


