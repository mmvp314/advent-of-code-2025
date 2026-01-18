import numpy as np
import pandas as pd
import re

df = pd.read_csv('.\data\day2_data.csv', sep="-",lineterminator=',',names=['start','end'], header=None)


# Part 1

res = 0

for i in range(len(df)):
    for j in range(df.start[i], df.end[i]+1):
        s = str(j)
        if len(s) % 2 == 0:
            if s[:len(s)//2] == s[len(s)//2:]:
                res += j

print(f"Part 1 answer: {res}")

# Part 2

res = 0

for i in range(len(df)):
    for j in range(df.start[i], df.end[i]+1):
        s = str(j)
        match = re.fullmatch(r"(.+)\1+", s)
        # Check for one or more occurrences of a substring followed by itseld

        if match:
            res += int(match[0])

print(f"Part 2 answer: {res}")
