import pandas as pd
import numpy as np

with open('./data/day5_data.txt', 'r') as file:
    lines = file.readlines()

ranges = []
ingredients = []

i=0
l = lines[i]

while l != "\n" and i < len(lines):
    ranges.append(tuple(map(int, l[:-1].split('-'))))
    i += 1
    l = lines[i]

for j in range(i+1, len(lines)):
    ingredients.append(int(lines[j][:-1]))

ranges.sort(key=lambda x:x[1])
ranges.sort(key=lambda x:x[0])

# Part 1

max_all = max(x[1] for x in ranges)

fresh = 0

for ing in ingredients:
    k=0
    (min1, max1) = ranges[k]
    if ing > max_all:
        continue
    while ing >= min1 and k < len(ranges):
        if ing > max1:
            k += 1
            (min1, max1) = ranges[k]
        else:
            fresh += 1
            break

print(fresh)

# Part 2

res = 0

current_range = [ranges[0][0], ranges[0][1]]

i=0
while i < len(ranges)-1 :
    if ranges[i][1] >= ranges[i+1][0]:
        current_range[1] = max(ranges[i][1], ranges[i+1][1])
        i += 1
    else:
        res += current_range[1] - current_range[0] + 1
        i += 1
        current_range = [ranges[i][0], ranges[i][1]]

if ranges[-2][0] < ranges[-1][0]:
    res += ranges[-1][1] - ranges[-1][0] + 1

print(res)
