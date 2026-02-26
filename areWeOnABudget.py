import sys
import math

cases = int(input())
for x in range(cases):
    numItems = int(input()) 
    strBudget = input().split(" ")
    strActual = input().split(" ")
    fBudget = list(map(float, strBudget))
    fActual = list(map(float, strActual))
    totalDiff = 0.00
    for i in range(numItems):
        totalDiff += round(fActual[i] - fBudget[i], 2)  
    roundDiff = round(totalDiff/numItems, 2)
    print(f"{roundDiff:.2f}")    