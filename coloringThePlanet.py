import math
import sys

def lerp(a,b,t):
    scalet = 0.0
    newpoint = []
    for p in range(1,3):
        var = (1-t)*a[p] + t*b[p]
        newpoint.append(var)


cases  = int(input(""))
for x in range(cases):
    line1 = list(map(int, input().split(" ")))
    cs = []
    controlPts = []
    temp = 0
    for i in range(line1[0]):
        thisLine = list(map(float, input().split(" ")))
        controlPts.append(thisLine)
        cs.append(thisLine[0])
    temp = int(input())
    tempscale = round((temp - line1[1])/(line1[2] - line1[1]), 2)
    cs.append(tempscale)
    cs.sort()
    indexes = [cs.index(tempscale) - 1, cs.index(tempscale)]
    newpoint = []
    for p in range(1,4):
        var = (1-tempscale)*controlPts[indexes[0]][p] + tempscale*controlPts[indexes[1]][p]
        var = math.floor(var)
        newpoint.append(var)
    # strList = " ".join(newpoint)
    for r in range(len(newpoint)):
        if(r != len(newpoint)):
            print(newpoint[r], end= " ")
        else:
            print(newpoint[r], "\n")
