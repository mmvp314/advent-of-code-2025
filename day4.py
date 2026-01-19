import pandas as pd
import numpy as np

with open('./data/day4_data.txt', 'r') as file:
    input = file.readlines()

n_rows = len(input)
n_cols = len(input[0]) - 1

input01 = np.zeros((n_rows+2, n_cols+2), dtype=int)

for i in range(n_rows):
    input01[i+1] = [0] + [1 if j == "@" else 0 for j in input[i]]

# Part 1

res = 0
for i in range(1,n_rows+1):
      for j in range(1,n_cols+1):
        if input01[i,j] == 1 and np.sum(input01[i-1:i+2,j-1:j+2]) - 1 < 4:
                res += 1

print(res)

# Part 2

res = 0
add = 99

while add > 0:
    add = 0
    for i in range(1,n_rows+1):
        for j in range(1,n_cols+1):
            if input01[i,j] == 1 and np.sum(input01[i-1:i+2,j-1:j+2]) - 1 < 4:
                    add += 1
                    input01[i,j] = 0
    print(add)
    res += add

print(res)