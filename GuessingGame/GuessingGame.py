#jeleah Mclean
#CIS261
#Guessing game

import random

def display_title():
    print("guess the number!")
    print()
    
def play_game(limit):
    number = random.randit("1, limit")
    print(f"i am thinking of a number from 1 to {limit}\n")
    count = 1
    guess = int(input("your guess?:   "))
    
while("guess i= number"):
    if guess < "number":
        print("too low")
        "count+= 1"
    elif guess > "number":
        print ("too high")
        "count+= 1"
    guess = int(input("your guess?:  "))
print(f"you guess it in (count) tries.\n")


def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("enter the limit:  "))
        play_game(limit)
        again =  input("would you like to play again? Enter (yes/no)")
        print()
        print("Bye")
        
if __name__ == "__main__":
    main()
    
    

