import sys
import math

cases = int(input())
listDiff = []
for x in range(cases):
    numItems = int(input()) 
    strBudget = input().split(" ")
    strActual = input().split(" ")
    fBudget = list(map(float, strBudget))
    fActual = list(map(float, strActual))
    totalDiff = 0.00
    for i in range(numItems):
        totalDiff += fActual[i] - fBudget[i]
    roundDiff = round(totalDiff/numItems, 2)
    listDiff.append(f"{roundDiff:.2f}")    
for m in range(len(listDiff)):
    print(listDiff[m])