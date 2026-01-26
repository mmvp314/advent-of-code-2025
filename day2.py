import numpy as np
import pandas as pd
import re

with open('./data/day2_data.txt', 'r',) as file:
    data = file.read()
    data = data.split(",")
    df_start = [int(line[:line.index("-")]) for line in data]
    df_end = [int(line[line.index("-")+1:]) for line in data]

# Part 1

res = 0

for i in range(len(data)):
    for j in range(df_start[i], df_end[i]+1):
        s = str(j)
        if len(s) % 2 == 0:
            if s[:len(s)//2] == s[len(s)//2:]:
                res += j

print(f"Part 1 answer: {res}")

# Part 2

res = 0

for i in range(len(data)):
    for j in range(df_start[i], df_end[i]+1):
        s = str(j)
        match = re.fullmatch(r"(.+)\1+", s)
        # Check for one or more occurrences of a substring followed by itseld

        if match:
            res += int(match[0])

print(f"Part 2 answer: {res}")
