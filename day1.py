import numpy as np
import pandas as pd

with open('./data/day1_data.txt', 'r') as file:
    data = [(-1*(line[0]=="L")+1*(line[0]=="R"))*int(line[1:-1]) for line in file]

# Part 1

res = 0
ptr = 50

for i in range(len(data)):
    # print(f"Start: {ptr}, increment: {data[i]}")
    ptr = (ptr + data[i]) % 100
    if ptr == 0:
        res += 1

print(res)

# Part 2

res = 0
ptr = 50

for i in range(len(data)):
    end = (ptr + data[i]) % 100 # final position of the pointer
    res += abs((ptr + data[i]) // 100) + (end == 0)
    res -= 1*(ptr == 0 and data[i] < 0) # extra rotation is counted when the pointer is at 0 and is rotated to the left
    res -= 1*(end == 0 and data[i] > 0) # extra rotation is counted when the pointer arrives at 0 after a rotation to the right
    ptr = end

print(res)