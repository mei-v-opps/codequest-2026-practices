import sys

cases = int(input(""))
finalAngles = []
for i in range(cases):
    anglesString = input("").split(" ")
    fangles = list(map(float, anglesString))
    for l in range(len(fangles)):
        if(fangles[l] < 0):
            fangles[l] = round(360 + fangles[l], 2)
            if(fangles[l] - 180 < 0):
                fangles[l] = round(360 + (fangles[l]-180.0), 2)
            else:
                fangles[l] = round(fangles[l] - 180.0, 2)
        else:
            if(fangles[l] - 180 < 0):
                fangles[l] = round(360 + (fangles[l]-180.0), 2)
            else:
                fangles[l] = round(fangles[l] - 180.0, 2)
    for p in range(len(fangles)):
        if(fangles[p] >= 100.00):
            anglesString[p] = str(fangles[p])
        elif(fangles[p] >= 10.00):
            anglesString[p] = "".join(["0", str(fangles[p])])
        else:
            anglesString[p] = "".join(["00", str(fangles[p])])
    anglesString = list(map(str, fangles))
    finalAngles.append(anglesString)
for m in range(len(finalAngles)):
    print(" ".join(finalAngles[m]))