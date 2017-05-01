# Matthew Tan
# mxtan@ucsc.edu
# pa3
# This creates a guessing game using python.

from random import *

guess1 = 0
guess2 = 0
guess3 = 0

num = randint(1, 10)
loseString = "\nYou lose. The number was " + str(num) + "."

print("I am thinking of an integer in the range", end="")
print(" 1 to 10. You have three guesses.")
print("")

guess1 = int(input("Enter your first guess: "))
if guess1 == num:
    print("You win!" + "\n")
elif guess1 > num:
    print("Your guess is too high." + "\n")
    guess2 = int(input("Enter your second guess: "))
    if guess2 == num:
        print("You win!" + "\n")
    elif guess2 > num:
        print("Your guess is too high." + "\n")
        guess3 = int(input("Enter your third guess: "))
        if guess3 == num:
            print("You win!" + "\n")
        elif guess3 > num:
            print("Your guess is too high.")
            print(loseString + "\n")
        elif guess3 < num:
            print("Your guess is too low.")
            print(loseString + "\n")
    elif guess2 < num:
        print("Your guess is too low." + "\n")
        guess3 = int(input("Enter your third guess: "))
        if guess3 == num:
            print("You win!")
        elif guess3 > num:
            print("Your guess is too high.")
            print(loseString + "\n")
        elif guess3 < num:
            print("Your guess is too low.")
            print(loseString + "\n")
elif guess1 < num:
    print("Your guess is too low." + "\n")
    guess2 = int(input("Enter your second guess: "))
    if guess2 == num:
        print("You win!" + "\n")
    elif guess2 > num:
        print("Your guess is too high." + "\n")
        guess3 = int(input("Enter your third guess: "))
        if guess3 == num:
            print("You win!" + "\n")
        elif guess3 > num:
            print("Your guess is too high.")
            print(loseString + "\n")
        elif guess3 < num:
            print("Your guess is too low.")
            print(loseString + "\n")
    elif guess2 < num:
        print("Your guess is too low." + "\n")
        guess3 = int(input("Enter your third guess: "))
        if guess3 == num:
            print("You win!" + "\n")
        elif guess3 > num:
            print("Your guess is too high.")
            print(loseString + "\n")
        elif guess3 < num:
            print("Your guess is too low.")
            print(loseString + "\n")
