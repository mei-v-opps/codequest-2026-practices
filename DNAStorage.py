import math
import sys

cases = int(input())
for z in range(cases):
    line = list(input().upper())
    bits = []
    for i in range(len(line)):
        if(line[i] == "G" or line[i] == "C"):
            line[i] = "1"
        elif(line[i] == "A" or line[i] == "T"):
            line[i] = "0"
    for i in range(0,len(line), 7):
        bits.append("".join([line[i], line[i+1], line[i+2], line[i+3], line[i+4], line[i+5], line[i+6]]))
    for i in range(len(bits)):
        bits[i] = chr(int(bits[i],2))
    print("".join(bits))