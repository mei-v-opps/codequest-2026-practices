import math
import sys

cases = int(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for z in range(cases):
    word = list(input())
    dots = 0
    for i in range(len(word)):
        for r in range(len(alpha)):
            if(alpha[r] == word[i]):
                dots += r+1
    print(dots)