from random import randint
from art import logo
EASY_TURNS = 10
HARD_TURNS = 5
def check(guess,answer,turns):
    if guess>answer:
        print("Too High!")
        return turns-1
    elif guess<answer:
        print("Too Low!")
        return turns-1
    else:
        print(f"The number was {answer}.You guessed it right!")
def set_difficulty():
    set = input("Enter 'easy' or 'hard'")
    if set == "easy":
        return EASY_TURNS
    elif set == "hard":
        return HARD_TURNS
def game():
    print(logo)
    answer = randint(1,100)
    print("Welcome to the guessing game! Guess a number from to 1 to 100!")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} number of turns left!")
        guess = int(input("Enter your guessed number: "))

        turns = check(guess,answer,turns)
        if turns == 0:
            print(f"You ran out of turns! You Losse! The number was {answer} ")
            return 0
        else:
            print("Guess Again!")
game()