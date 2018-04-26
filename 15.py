#Caleb Smith-Salzberg
#SoftDev2 pd7
#K15 -- Do You Even List?
#2018-04-25

import math

upper = "ABCDEFGHIJKLMNOPQRSTUVWXTYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = ".?!&#,;:-_*"

def pcheck(pword):
    all = [1 if x in upper else 2 if x in lower else 3 if x in num else 0 for x in pword]
    return (1 in all and 2 in all and 3 in all)

print pcheck("Hell0")

def prate(pword):
    lengthPtsL = [.5 for x in pword]
    if len(pword) > 12:
        lengthPts = 6
    else :
        lengthPts = math.floor(len(lengthPtsL) * .5)
    upperPts = 1 in [1 for x in pword if x in upper]
    lowerPts = 1 in [1 for x in pword if x in lower]
    numPts = 1 in [1 for x in pword if x in num]
    specialPts = 1 in [1 for x in pword if x in special]
    return lengthPts + upperPts + lowerPts + numPts + specialPts

print prate("He9?")
