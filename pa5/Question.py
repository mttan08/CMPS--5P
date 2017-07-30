# Matthew Tan
# mxtan@ucsc.edu
# programming assignment 5
# Plays the user version of the game. You know the number, the computer
# tries to guess it using by the binary search algorithm.

import math

Lst = []
low = 0
high = 0
midpoint = 0
guess = 0
midpointIndex = 0

def binSearch(x, L):
    left = 0
    right = len(L) - 1
    while left <= right:
        m = (left + right) // 2
        if x == L[m]:
            return m
        elif x < L[m]:
            right = m - 1
        else:
            left = m + 1

def getMidpoint():        
    if len(Lst) == 0:
        print("Your answers have not been consistent.")
        print("")
        print("")
        return -1
    #if len(Lst) % 2 == 0:                    
    #    midIndex = (len(Lst)) // 2 - 1
    #elif len(Lst) % 2 == 1:
    #    midIndex = (len(Lst)) // 2
    midIndex = math.ceil(len(Lst) / 2) - 1
    midpointIndex = binSearch(Lst[midIndex], Lst)
    midpoint = Lst[midpointIndex]
    if len(Lst) == 1:
        print("Your number is " + str(midpoint) + "." + " I found it in " 
             + str(guess) + " guesses.")
        print("")
        print("")
        return -1
    print("Is your number Less than, Greater Than, or Equal to " 
          + str(Lst[midpointIndex]) + "?")
    return midpointIndex
# -- main program ----------------------------------------------------------
print("")
print("")
print("Enter two numbers, low then high.")
while True:
    low = int(input("low = "))
    high = int(input("high = "))
    print("")
    if low > high:
        print("Please enter the smaller followed by the larger number.")
    elif low < high:
        midpoint = (low + high) // 2
        print("Think of a number in the range " + str(low) + " to " 
        + str(high) + ".")
        print("")
        for low in range(low, high + 1):
            Lst.append(low)
        #if len(Lst) % 2 == 0:
        #    midpointIndex = len(Lst) // 2 - 1
        #else:
        #    midpointIndex = len(Lst) // 2
        midpointIndex = math.ceil(len(Lst) / 2) - 1
        print("Is your number Less than, Greater than, or Equal to " 
            + str(midpoint) + "?")
        string = input("Type 'L', 'G', or 'E': ")
        print("")
        upperString = string.upper()
        lgeString = "LGE"
        while True:
            if upperString.upper() not in lgeString:
                upperString = input("Please type 'L', 'G', or 'E': ")
                print("")
            else:
                guess += 1
                tempString = upperString
                if tempString.upper() == "E":
                    if guess == 1:
                        print("I found your number in " + str(guess) 
                        + " guess.")
                        print("")
                        print("")
                    elif guess > 1:
                        print("Your number is " + str(Lst[midpointIndex]) 
                        + "." + " I found your number in " + str(guess) 
                        + " guesses.")
                        print("")
                        print("")
                    break
                elif tempString.upper()== "L":
                    leftList = []
                    for i in range(0, midpointIndex):
                        leftList.append(Lst[i])
                    Lst = leftList
                    midpointIndex = getMidpoint()
                    if midpointIndex == -1:
                        break
                    upperString = input("Type 'L', 'G', or 'E': ")
                    print("")
                elif tempString.upper() == "G":
                    rightList = []
                    for i in range(midpointIndex + 1, len(Lst)):
                        rightList.append(Lst[i])
                    Lst = rightList
                    midpointIndex = getMidpoint()
                    if midpointIndex == -1:
                        break
                    upperString = input("Type 'L', 'G', or 'E': ")
                    print("")
        break
    elif low == high:
        midpoint = (low + high) // 2
        print("Think of a number in the range " 
        + str(low) + " to " + str(high) 
          + ".")
        print("")
        print("Your number was " + str(low) + "." + " I found it in " 
        + str(guess) + " guesses.")
        print("")
        print("")
        break
