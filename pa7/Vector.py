"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""

# Matthew Tan
# mxtan@ucsc.edu
# programming assignment 7
# Returns a module called Vector that returns a series of vector operations.

#---------------------------------------------------------------------------
# import standard library modules
#---------------------------------------------------------------------------

import math
import random

#---------------------------------------------------------------------------
# function definitions
#---------------------------------------------------------------------------

def add(u, v):
    """
    Return the vector sum u+v.
    """
    C = []
    for i in range(len(u)):
        C.append(u[i] + v[i])
    return C
# end add()

def negate(u):
    """
    Return the negative -u of the vector u.
    """
    negVector = u[:]
    for i in range(len(u)):
        negVector[i] = -negVector[i]
    return negVector
# end negate()   

def sub(u, v):
    """
    Return the vector difference u-v.
    """
    return add(u, negate(v))
# end sub()

def scalarMult(c, u):
    """
    Return the scalar product cu of the number c by the vetor u.
    """
    x = u[:]
    for i in range(len(x)):
        x[i] = c * x[i]
    return x
# end scalarMult()

def zip(u, v):
    """
    Return the component-wise product of u with v.
    """        
    C = []
    for i in range(len(u)):
        C.append(u[i] * v[i])
    return C
# end zip()

def dot(u, v):
    """
    Return the dot product of u with v.
    """
    a = u[:]
    b = v[:]
    c = zip(a, b)
    sumNums = 0
    for i in range(len(c)):
        sumNums += c[i]
    return sumNums
# end dot()

def length(u):
    """
    Return the (geometric) length of the vector u.
    """
    a = u[:]
    b = dot(a, a)
    c = math.sqrt(b)
    return c
# end length()
   
def unit(v):
    """
    Return a unit(geometric length 1) vecotr in the direction of v.
    """
    a = v[:]
    b = length(a)
    for i in range(len(a)):
        a[i] = a[i] / b
    return a
# end unit()

def angle(u, v):
   """
   Return the angle (in degrees) between vectors u and v.
   """
   return math.degrees(math.acos(dot(unit(u),unit(v))))
# end angle()

def randVector(n, a, b):
    """
    Return a vector of dimension n whose components are random floats 
    in the range [a, b).
    """
    randVector = []
    for i in range(n):
        randVector.append(random.uniform(a,b))
    return randVector 
# end randomVector()
