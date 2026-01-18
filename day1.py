import numpy as np
import pandas as pd

df = pd.read_csv('.\data\day1_data.csv', names=['lr'], header=None)
df = df.replace("R","", regex=True).replace("L", "-", regex=True)
df = df.astype(int)

# Part 1

res = 0
ptr = 50

for i in range(len(df)):
    # print(f"Start: {ptr}, increment: {df.lr[i]}")
    ptr = (ptr + df.lr[i]) % 100
    if ptr == 0:
        res += 1

print(res)

# Part 2

res = 0
ptr = 50

for i in range(len(df)):
    end = (ptr + df.lr[i]) % 100 # final position of the pointer
    res += abs((ptr + df.lr[i]) // 100) + (end == 0)
    res -= 1*(ptr == 0 and df.lr[i] < 0) # extra rotation is counted when the pointer is at 0 and is rotated to the left
    res -= 1*(end == 0 and df.lr[i] > 0) # extra rotation is counted when the pointer arrives at 0 after a rotation to the right
    ptr = end

print(res)