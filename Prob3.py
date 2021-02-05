import numpy as np
#random.uiniform will produce random float values from 1 -20
x = np.random.uniform(1,high=20, size=20)
a = x.reshape(4, 5)
# np.amax will get the max values of each row,for that we need to give axis=1
row_maxes = np.amax(a, axis=1)
#reshape(-1,1) will arrange the array in undefined row(-1) and one column(1) , and replace with zero
b = np.where(a == row_maxes.reshape(-1,1),0,a)
print("replaced highest row value by zero")
print(b)

