#THIS FILE IS A COPY OF SOMEONE ELSES

import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

#finds the target temp on the scale
def find_rel_val(value, min, max):
    return (value - min) / (max - min)

#plugs in to interpolate the value but what are they using for a and b??
def lerp(a, b, t):
    return (1 - t) * a + t * b

for _ in range(int(input())):
    #splits the fist line into what we need i have this but in a diff form
    N, L, H = map(int, input().split())
    control_points = [] 
    for _ in range(N):
        #splits each line into the position r,b,g
        position, R, G, B = map(float, input().split())
        R, G, B = map(int, (R, G, B))
        #adds it to the list
        control_points.append([position, R, G, B])
    #takes the target temp
    temp = int(input())
    #finds where the target temp is on the scale
    finded_position = find_rel_val(temp, L, H)
    for i in range(N - 1): #<----- for however many points they give you
        #finds between which two points is the target point
        if control_points[i][0] <= finded_position and control_points[i + 1][0] >= finded_position:
            #eliminates the other points and leaves the ones that matter/the two points the target is between
            control_points = [control_points[i], control_points[i + 1]]
            break
    ranges = find_rel_val(finded_position, control_points[0][0], control_points[1][0])
    print(ranges)
    output = [str(math.floor(lerp(control_points[0][i + 1], control_points[1][i + 1], ranges))) for i in range(3)]
    print(' '.join(output))