import numpy as np
import pandas as pd

with open('./data/day3_data.txt', 'r') as file:
    df = [line[:-1] for line in file]

# Part 1

res = 0

for i in df:
    s = list(str(i))
    max1 = max(s[:-1])
    index1 = s.index(max1)
    res += int(max1)*10

    max2 = max(s[index1 + 1:])
    res += int(max2)

print(f"Part 1 answer: {res}")

# Part 2

res = 0

for i in df:
    res1 = ''
    s = str(i)
    j = 12
    while len(s) > j and j>1:
        max1 = max(s[:-j+1])
        res1 += max1
        index1 = s.index(max1)
        s = s[index1+1:]
        j -= 1
    if j==1:
        res1 += max(s)
    else:
        res1 += s
    res += int(res1)

print(f"Part 2 answer: {res}")
