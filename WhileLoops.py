import random

print("Welcome to my guessing game")
print("Guess the number between 1 and 100 I am thinking of.")
number = random.randint(1,100)
guess = -1
while guess != number:
    guess_str = input("Guess the number:")
    guess = int(guess_str)
