from random import randint #return random integer from range
from replit import clear
from guessart import logo

EASY_LEVEL_ATTEMPT = 10
HARD_LEVEL_ATTEMPT = 5
random_num  = randint(1, 50)

def guess_number():
    print(logo)
    def check_guess(user_guess, random_num, attempt:int):
        if user_guess > random_num:
            print("Too high")
            return attempt - 1
        
        elif user_guess < random_num:
            print("Too low")
            return attempt - 1
        
        else:
            print(f"You Guessed it Correctly ! The number was {random_num}")        
            
    def difficulty_level():
        user_choice = input("Choose a level you want to play 'Easy' or 'Hard' : ").lower()
        if user_choice == "Easy":
            return EASY_LEVEL_ATTEMPT
        else:
            return HARD_LEVEL_ATTEMPT
    
    print("Number guessing Game")
    attempt = difficulty_level()
    print("Guess the number between 1 and 50")  


    while not attempt == 0:       
        user_guess = int(input("Make a Guess : "))
        attempt = check_guess(user_guess, random_num, attempt)
        print(f"You have {attempt} attempt remaining to guess the number")

        if attempt == 0:
            print("You run out of guesses you lose")
            want_play = input("Do you want to play again from start enter 'yes' to continue and 'no' to exit : ")
            if want_play == "yes":
                clear()
                guess_number()
            else:
                clear()
            

guess_number()