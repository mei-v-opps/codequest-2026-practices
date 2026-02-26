import sys

cases = int(input(""))
finalAngles = []
for i in range(cases):
    anglesString = input("").split(" ")
    fangles = list(map(float, anglesString))
    for l in range(len(fangles)):
        if(fangles[l] - 180 < 0):
            fangles[l] = round(360 + (fangles[l]-180.0), 2)
        else:
            fangles[l] = round(fangles[l] - 180.0, 2)
    anglesString = list(map(str, fangles))
    finalAngles.append(anglesString)
for m in range(len(finalAngles)):
    print(" ".join(finalAngles[m]))