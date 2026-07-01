import numpy as np
# Array of random integers between 1 and 50 of size 20
arr = np.random.randint(1, 51, 20)
# Reshape into 4x5
matrix = arr.reshape(4, 5)
print("Matrix")
print(matrix)
print("\nSum:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard Deviation:", matrix.std())
print("\nMaximum Value in Each Row")
print(matrix.max(axis=1))