import numpy as np
import pandas as pd
from functools import lru_cache

with open('./data/day7_data.txt', 'r') as file:
    lines = file.readlines()

data = np.empty((len(lines), len(lines[0]) - 1), 
                dtype=str)

for i in range(len(lines)):
    data[i] = np.array(list(lines[i][:-1]))

S = np.where(data[0] == "S")
data[1][S] = "|"
print(len(data))

for i in range(2,len(data)):
    for j in range(len(data[i])):
        if data[i-1][j] == "|":
            if data[i][j] == ".":
                data[i][j] = "|"
            elif data[i][j] == "^":
                data[i][j-1:j+2] = ["|","^","|"]

# Part 1

res = 0

splitters = np.where(data == "^")

for i in range(len(splitters[0])):
    (j,k) = (splitters[0][i], splitters[1][i])
    if data[j-1,k] == "|":
        res += 1

print(res)

# Part 2

paths = 0

@lru_cache
def follow(i, j, paths):
    if i == len(data)-1:
        # print(f"(i,j,paths)={(i,j,paths)}")
        return 1
    else:
        if data[i+1][j] == "|":
            i += 2
            return follow(i, j, paths)
        elif data[i+1][j] == "^":
            i += 2
            return follow(i, j-1, paths) + follow(i, j+1, paths)
    return paths

i = 1
j = int(np.where(data[i] == "|")[0][0])

paths += follow(i, j, paths)

print(paths)