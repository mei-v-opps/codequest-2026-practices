import math
import sys

cases = int(input())
for z in range(cases):
    sentences = int(input())
    allchar = []
    letters =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(sentences):
        sentence = input()
        line = "".join(e for e in sentence if e.isalpha())
        line = line.upper()
        line = [char for char in line]
        allchar+=line
    for m in range(len(letters)):
        count = 0
        for n in range(len(allchar)):
            if(allchar[n] == letters[m]):
                count+=1
        count = (count/len(allchar))*100
        count = round(count, 2)
        print(f"{letters[m]}: {count:.2f}%")        
        