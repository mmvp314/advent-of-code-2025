import numpy as np
import pandas as pd
import math

with open('./data/day8_data.txt','r') as file:
    data = [line[:-1].split(',') for line in file]
    data = [[int(a), int(b), int(c)]  for (a,b,c) in data]

# Array of distances = concatenation of upper triangular matrix of distances with inf replacing 0
distances = np.concat([[math.inf]*(i+1) + [math.dist(data[i], data[j]) for j in range(i+1,len(data))] for i in range(len(data))])

n_connections = 1000
n_circuits = 3
# Indices of shortest distances in the array
n_closest = distances.argsort()[:n_connections]

def int_to_coord(i):
    # Convert array index to tuple of box IDs
    return(i//len(data), i%len(data))

n_closest = [int_to_coord(x) for x in n_closest]

# Dictionary where keys = box IDs, items = circuit in which they are
dict_box = {i: i for i in range(len(data))}

# Dictionary where keys = circuit ID, items = {boxes in that circuit}
dict_circuits = {i: {i} for i in range(len(data))}

for (p,q) in n_closest:
    if dict_box[p] != dict_box[q]:
        c = dict_box[p]

        # Concatenate the circuits
        dict_circuits[dict_box[q]].update(dict_circuits[c])

        # Update circuit IDs to which boxes are associated
        for r in dict_circuits[c]:
            dict_box[r] = dict_box[q]
        
        # Reset one of the two circuits
        dict_circuits[c] = set()
        
circuit_lengths = [len(dict_circuits[x]) for x in dict_circuits.keys()]

res = math.prod(sorted(circuit_lengths, reverse=True)[:n_circuits])

print(res)

# Part 2

n_closest = distances.argsort()
n_closest = [int_to_coord(x) for x in n_closest]

dict_box = {i: i for i in range(len(data))}
dict_circuits = {i: {i} for i in range(len(data))}

longest_circuit = set()
current_pq = (0,0)

i = 0
while len(longest_circuit) < len(data):
    (p,q) = n_closest[i]
    current_pq = (p,q)
    if dict_box[p] != dict_box[q]:
        c = dict_box[p]

        # Concatenate the circuits
        dict_circuits[dict_box[q]].update(dict_circuits[c])

        # Update circuit IDs to which boxes are associated
        for r in dict_circuits[c]:
            dict_box[r] = dict_box[q]
        
        # Reset one of the two circuits
        dict_circuits[c] = set()
        
    if len(dict_circuits[dict_box[q]]) > len(longest_circuit):
        longest_circuit = dict_circuits[dict_box[q]]
    i+=1

(p,q) = current_pq
res = data[p][0] * data[q][0]
print(res)