import math
import sys

def findRelVal(t, min, max):
    return (t - min)/(max - min)

def lerp(a, b, t):
    return (1-t)*a + t*b

cases  = int(input(""))
for x in range(cases):
    N, L, H = map(int, input().split(" "))
    controlPoints = []
    for i in range(N):
        position, R, G, B = map(float, input().split())
        R,G,B = map(int, (R, G, B))
        controlPoints.append([position, R, G, B])
    temp = int(input())
    temp = findRelVal(temp, L, H)
    for m in range(N-1):
        if(temp >= controlPoints[m][0] and temp <= controlPoints[m+1][0]):
            controlPoints = [controlPoints[m], controlPoints[m+1]]
            break
    relVal = findRelVal(temp, controlPoints[0][0], controlPoints[1][0])
    newPoint = []
    for n in range(1,4):
        newPoint.append(math.floor(lerp(controlPoints[0][n], controlPoints[1][n], relVal)))
    newPoint = list(map(str, newPoint))
    print(" ".join(newPoint))