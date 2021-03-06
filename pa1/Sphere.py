# Matthew Tan
# mxtan@ucsc.edu
# programming assignment 1
# This takes user input and calculates the volume and surface area of a sphere.

from math import pi as p

r = float(input("Enter the radius of the sphere: "))
volume = (4.0 / 3.0) * p * r**3
surfaceArea = 4 * p * r**2

print("The volume is: " + str(volume))
print("The surface area is: " + str(surfaceArea))
