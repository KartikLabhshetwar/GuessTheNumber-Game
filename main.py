import random
from art import logo
print(logo)

#here the computer randomly chooses the number.
def guess_number():
    number = list(range(1,101))
    return random.choice(number)
random_number = guess_number()

#beginning of the game.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
a = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if a == 'hard':
    
    count = 5
    while count:
        print(f"You have {count} attempts remaining to guess the number.")
        b = int(input("Make a guess: "))
        if b == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        if random_number > b:
            print("Too Low.\nGuess again.")
        elif random_number < b:
            print("Too High.\nGuess again.")
        count -= 1 
    if count == 0:
        print("You've run out of guesses. You lose.")
        
elif a == 'easy':
    
    count = 10
    while count:
        print(f"You have {count} attempts remaining to guess the number.")
        b = int(input("Make a guess: "))
        if b == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        if random_number > b:
            print("Too Low.\nGuess again.")
        elif random_number < b:
            print("Too High.\nGuess again.")
        count -= 1
    if count == 0:
        print("You've run out of guesses. You lose.")
