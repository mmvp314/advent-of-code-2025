import numpy as np
import pandas as pd

df = pd.read_csv('.\data\day1_data.csv', names=['lr'], header=None)
df = df.replace("R","", regex=True).replace("L", "-", regex=True)
df = df.astype(int)

res = 0
ptr = 50

for i in range(len(df)):
    # print(f"Start: {ptr}, increment: {df.lr[i]}")
    ptr = (ptr + df.lr[i]) % 100
    if ptr == 0:
        res += 1

print(res)