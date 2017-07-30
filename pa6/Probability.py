# Matthew Tan
# mxtan@ucsc.edu
# programming assignment 6
# Calculates the sum, frequency, relative frequency, and
# experimental probability of m dice with k sides.

import random

randInt = random.Random(237)

# throwDice(m, k)
# returns a tuple of m dice of k sides
def throwDice(m, k):
    die = []
    #print("In throwDice(): dice is: ", dice)
    for i in range(1, m + 1):
        die.append(randInt.randrange(1, k + 1))
    #print("In throwDice(): dice is: ", dice)
    return tuple(die)
# end throwDice()

#-- main --------------------------------------------------------------------

# print(throwDice(numDice, numSides)) # for testing purposes

print("")
numDie = int(input("Enter number of dice: "))
while True:
    if numDie < 1:
        print("The number of dice must be at least 1")
        numDie = int(input("Please enter the number of dice: "))
    else:
        break
print("")

numSides = int(input("Enter the number of sides on each die: "))
while True:
    if numSides < 2:
        print("The number of sides must be at least 2")
        numSides = int(input("Please enter the number of sides: "))
    else:
        break
print("")

numTrials = int(input("Enter the number of trials to perform: "))
while True:
    if numTrials < 2:
        print("The number of trials  must be at least 1")
        numTrials = int(input("Please enter the number of trials to perform: "))
    else:
        break
print("")

# perform simulation, record and print frequencies
listOfDie = numDie * numSides + 1
frequency = listOfDie * [0]
for i in range(numTrials):
    throw = throwDice(numDie, numSides)
    #print("in main: throw is: ", throw)
    index = 0
    for j in range(numDie):
        index += throw[j]
    frequency[index] += 1
    #print("in main: index is: ", index)
#print("[", end="")
#for i in range(len(frequency)):
#    print(i, end=", ")
#print("]", end="")
#print("")
#print("Frequencies:")
#print(frequency)

# calculate relative frequencies and experimetal probabilities
relativeFrequency = numDie* [0]
experimentalProbability = numDie* [0]
for i in range(numDie, len(frequency)):
    relativeFrequency.append(frequency[i] / numTrials)
    experimentalProbability.append(relativeFrequency[i] * 100)

#print("Relative Frequency:")
#print(relativeFrequency)
#print("length of relative frequency:", len(relativeFrequency))

#print("")
#print("Experimental Probability:")
#print(experimentalProbability)
#print("length of experimental probability:", len(experimentalProbability))

#print("length of frequency is: ", len(frequency))

# print results
f1 = " {0:<4}    {1:<5}     {2:<5}     {3:<5}"
f2 = 70 * "-"
f3 = "{0:>4}  {1:9}           {2:<11.5f}        {3:9.2f} %"
print(f1.format("Sum","Frequency","Relative Frequency","Experimental Probability"))
print(f2)
for i in range(numDie, len(frequency)):
    print(f3.format(i, frequency[i], relativeFrequency[i], experimentalProbability[i]))
print("")
