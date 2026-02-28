import sys
import math
from decimal import *
# ...

def round_half_up(num, dec):
    mult = 10 ** dec
    return math.floor(num * mult + 0.5) / mult

cases = int(input())
ans = []
for x in range(cases):
    numItems = int(input()) 
    strBudget = input().split(" ")
    strActual = input().split(" ")
    fBudget = []
    fActual = []
    for i in range(len(strBudget)):
        fBudget.append(Decimal(strBudget[i]))
        fActual.append(Decimal(strActual[i]))
    totalDiff = 0.00
    totalBudget = 0
    totalActual = 0
    for i in range(numItems):
        totalBudget += fBudget[i]
        totalActual += fActual[i]
    totalDiff = totalActual - totalBudget
    avgDiff = Decimal(totalDiff/numItems)
    roundDiff = avgDiff.quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
    print(f"{roundDiff:.2f}")    