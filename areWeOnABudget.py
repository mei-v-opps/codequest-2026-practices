import sys
import math
# ...

def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

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
        # totalDiff += fActual[i] - fBudget[i]
    totalDiff = totalActual - totalBudget
    roundDiff = round_half_up(totalDiff/numItems, 2)
    print(f"{roundDiff:.2f}")    