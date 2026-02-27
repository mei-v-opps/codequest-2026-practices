import sys
import math
# ...

def round_half_up(num, dec):
    mult = 10 ** dec
    return math.floor(num * mult + 0.5) / mult

cases = int(input())
for x in range(cases):
    numItems = int(input()) 
    strBudget = input().split(" ")
    strActual = input().split(" ")
    fBudget = list(map(float, strBudget))
    fActual = list(map(float, strActual))
    totalDiff = 0.00
    totalBudget = 0
    totalActual = 0
    for i in range(numItems):
        totalBudget += fBudget[i]
        totalActual += fActual[i]
    totalDiff = totalActual - totalBudget
    roundDiff = round_half_up(totalDiff/numItems, 2)
    print(f"{roundDiff:.2f}")    