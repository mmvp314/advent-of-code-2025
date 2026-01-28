import numpy as np
import math

with open("./data/day9_data.txt", 'r') as file:
    data = [line[:-1].split(",") for line in file]
    data = [[int(a), int(b)] for (a,b) in data]    

# Part 1

def area(x,y):
    return (abs(x[0]-y[0])+1) * (abs(x[1]-y[1])+1)

areas = np.concat([[0]*(i+1) + [area(data[i], data[j]) for j in range(i+1,len(data))] for i in range(len(data))])

res = np.max(areas)
print(res)

# Part 2

import shapely
from shapely import Polygon
shape = Polygon(data + [data[0]])

res = 0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        x = data[i]
        y = data[j]
        rect = shapely.box(min(x[0],y[0]),
                            min(x[1],y[1]),
                            max(x[0],y[0]),
                            max(x[1],y[1]))
        if area(data[i], data[j]) > res and shape.contains(rect):
            res = area(data[i], data[j])

print(res)
