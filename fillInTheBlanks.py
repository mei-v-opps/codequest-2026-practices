import math
import sys
import re

cases = int(input())
for z in range(cases):
    D, T = map(int, input().split(" "))
    positions = []
    info = []
    sentences = []
    for i in range(D):
        line = input().split(": ", maxsplit = 1)
        positions.append(line[0])
        info.append(line[1])
    for i in range(T):
        line1 = re.split(r'([\[\]])', input())
        sentences.append(line1)
    for i in range(len(sentences)):
        sentences[i] = [word for word in sentences[i] if word!="["]
        sentences[i] = [word for word in sentences[i] if word!="]"]
    for i in range(len(sentences)):
        for r in range(len(sentences[i])):
            for q in range(len(positions)):
                if(sentences[i][r] == "".join([positions[q]])):
                    sentences[i][r] = info[q]
    for i in range(len(sentences)):
        sentences[i] = "".join(sentences[i])
        print(sentences[i])
