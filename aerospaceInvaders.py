import math
#PRINT --> SUBTRACT --> SORT --> REPEAT
cases = int(input())
totalShips = []
for i in range(cases):
  ships = int(input())
  listShips = []
  for r in range(ships):
    newShip = input().split(":")
    shipName = newShip[0].split("_")
    coor = newShip[1].split(",")
    intC = list(map(int, coor))
    fullShip = [shipName, intC]
    if(fullShip[1][0] > 0):
      listShips.append(fullShip)

  for l in range(len(listShips)):
    swapped = False
    for j in range(len(listShips)-l-1):
      if(listShips[j][1][0] == listShips[j+1][1][0]):
        if(listShips[j][1][1] < listShips[j+1][1][1]):
          listShips[j], listShips[j+1] = listShips[j+1], listShips[j]
          swapped = True
        elif(listShips[j][1][0] > listShips[j+1][1][0]):
          listShips[j], listShips[j+1] = listShips[j+1], listShips[j]
          swapped = True
    if not swapped:
      break
  
  while (len(listShips) > 0):
    for l in range(len(listShips)):
      swapped = False
      for j in range(len(listShips)-l-1):
        if(listShips[j][1][0] == listShips[j+1][1][0]):
         if(listShips[j][1][1] < listShips[j+1][1][1]):
          listShips[j], listShips[j+1] = listShips[j+1], listShips[j]
          swapped = True
        elif(listShips[j][1][0] > listShips[j+1][1][0]):
          listShips[j], listShips[j+1] = listShips[j+1], listShips[j]
          swapped = True
      if not swapped:
        break
    if(listShips[0][1][0] > 0):
      totalShips.append(" ".join(["Destroyed Ship:", str(listShips[0][0][0]),"xLoc:", str(listShips[0][1][0])]))
    listShips.pop(0)
    for i in range(len(listShips)):
      if(listShips[i][0][1] == "A"):
        (listShips[i][1][0]) -= 10
      elif(listShips[i][0][1] == "B"):
        (listShips[i][1][0]) -= 20  
      elif(listShips[i][0][1] == "C"):
        (listShips[i][1][0]) -= 30

for q in range(len(totalShips)):
  print(totalShips[q])

  