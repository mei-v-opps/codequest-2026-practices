import math
import sys

cases = int(input())
for z in range(cases):
    L, C, N = map(int, input().split())
    statements = []
    ifs = []
    brackets = []
    nestcount = 0
    for i in range(L):
        line = input().lower().split()
        if(line[0] == "if" or line[0] == "{" or line[0] == "}" or line[0] == "else" or line[0] == "print"):
            statements.append(line[0])
            if(line[0] == "if" or line[0] == "else"):
                ifs.append(line[0])
            elif(line[0] == "{" or line[0] == "}"):
                brackets.append(line[0])
    for i in range(len(brackets)):
        thisncount = 1
        if(i < len(brackets)):
            if(brackets[i] == "{" and brackets[i+1] == "{"):
                thisncount+=1
                if(thisncount > nestcount):
                    nestcount = thisncount
     
    print(nestcount)
            
    print(statements)     
    