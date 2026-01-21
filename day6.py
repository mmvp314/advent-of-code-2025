import pandas as pd
import numpy as np
import math
import re

with open('./data/day6_data.txt', 'r') as file:
    lines = file.readlines()

# Part 1

data = []

for i in range(len(lines)-1):
    data.append(list(map(int, re.split(" +", lines[i][:-1]))))

data = np.array(data).transpose()

operations = re.split(" +", lines[-1][:-1])
operations.remove('')

res = 0

for i in range(len(data)):
    if operations[i] == "+":
        res += sum(data[i])
    else:
        res += math.prod(data[i])

print(res)

# Part 2

data = []

for i in range(len(lines)-1):
    data.append(list(lines[i][:-1]))

data = [''.join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]

res = 0

i = 0

for j in range(len(operations)):
    tmp = []
    while i < len(data) and data[i] != " "*4:
        tmp.append(int(data[i]))
        i += 1
    if operations[j] == "+":
        res += sum(tmp)
    else:
        res += math.prod(tmp)
    i += 1

print(res)