
from random import *
from art import logo

number = randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
guess = 0
n_try = 0
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
  n_try = 10
else:
  n_try = 5
print(f"You have {n_try} attempts remaining to guess the number.")
game_over = False
def guess_numb(number, n_try):
  guess = int(input("Make a guess: "))
  if guess == number:
    print(f"You got it! The answer was {number}.")
    game_over = True
  elif guess > number:
    print("Too high.")
    n_try -= 1
    print(f"You have {n_try} attempts remaining to guess the number.")
  elif guess < number:
    print("Too low.")
    n_try -= 1
    print(f"You have {n_try} attempts remaining to guess the number.")
  return n_try
  
while game_over == False:
  n_try = guess_numb(number, n_try)
  if n_try == 0:
    print(f"You've run out of guesses, you lose. The secret number was {number}")
    game_over = True
  
