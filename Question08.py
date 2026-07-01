import numpy as np
# 4x4 matrix of random integers between 1 and 100
arr = np.random.randint(1, 101, (4, 4))
print("Matrix")
print(arr)
print("\nShape:", arr.shape)
print("Dimension:", arr.ndim)
print("Total Elements:", arr.size)
print("Data Type:", arr.dtype)
print("Minimum Value:", arr.min())
print("Maximum Value:", arr.max())