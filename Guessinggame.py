#07032024
import random

print("Welcome to the Guessing game ")
print("Make a guess between 1 and 100")
system_guess=random.randint(0,100)
level=input("Choose a difficulty...type 'easy' or 'hard':\t").lower()
if level=='easy':
    attempts_left=7
else:
    attempts_left=5
print(f"you have {attempts_left} attempts left !")
print(system_guess)

def check(user_input,system_guess,attempts_left):
    if user_input>system_guess:
        print("Guessed too High")
        attempts_left -= 1 
        print(f"you have {attempts_left} attempts left !")
    elif user_input<system_guess:
        print("guessed too low")
        attempts_left -= 1
        print(f"you have {attempts_left} attempts left !")
    else:
        print("made the correct guess...You WIN")
        guess=True
    return attempts_left

guess=False

while not guess:
    if attempts_left>0:
        user_input=int(input("Make a guess:\t"))
        attempts_left=check(user_input,system_guess,attempts_left)
    else:
        print("You have run out of attempts.\nYou LOSE.")

