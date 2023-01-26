import random


print("Guess the Number \n")
game_level = input("Enter a game level You want to play 'Hard' or 'Easy' \n")
set_attempt = 0
if game_level == "hard":
    set_attempt = 5
elif game_level == 'easy':
    set_attempt = 10

print(f"Game Level Set on '{game_level} Level' You Have Total {set_attempt} Attempts")
user_guess = int(input("Enter Your Guess Number: "))

number_list = []
for num in range(user_guess + 1):
   number_list.append(num) 
    
#print(number_list)

random_number = random.choice(number_list)
#print(f"Random Number is {random_number}")

# def check_guess(random_number, user_guess):
while not set_attempt == 0:
    if random_number == user_guess:
        print("You Guessed it correctly! You Won the game!\n")
        set_attempt = 0
    else:   
        if random_number < user_guess:
            print("Too High")
            set_attempt = set_attempt - 1
            print(f"Attempt left {set_attempt}")
            
        if random_number > user_guess:
            print("Too Low")
            set_attempt = set_attempt - 1
            print(f"Attempt left {set_attempt}")
            
    user_guess = int(input("Make a guess again :"))
    
    if set_attempt == 0:
        print(f"Number was {random_number}😅\nYou Lost the Game 😐")
# check_guess(random_number, user_guess)




