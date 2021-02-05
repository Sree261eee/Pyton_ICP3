import numpy as np
x = np.random.uniform(1,high=20, size=20)
a = x.reshape(4, 5)
row_maxes = np.amax(a, axis=1)
b = np.where(a == row_maxes.reshape(-1,1),0,a)
print("replaced highest row value by zero")
print(b)
"""j=0
#print(max_index_row)
for i in max_index_row:
    a[j][i] = 0
    j+=1
print(a)
#result = np.where(np.amax(a, axis=1),[3])
index = np.max(a, axis=1)
row_maxes = a.max(axis=1)
#np.where(a == row_maxes, 1, 0)
print(np.where(index,0,a))
print(a)"""