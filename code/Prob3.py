import numpy as np
x = np.random.uniform(1,high=20, size=20)
a = x.reshape(4, 5)
row_maxes = np.amax(a, axis=1)
b = np.where(a == row_maxes.reshape(-1,1),0,a)
print("replaced highest row value by zero")
print(b)
