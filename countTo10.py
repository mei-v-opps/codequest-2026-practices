import math
import sys

cases = int(input())
for z in range(cases):
    bits = int(input())
    strB = []
    for i in range(bits):
        strB.append("1")
    strB = "".join(strB)
    targetNum = int(strB, 2)
    for i in range(targetNum+1):
        print(str(bin(i)[2:]).rjust(bits, "0"))