import numpy as np
# Random decimal numbers
arr1 = np.random.rand(10)
# Random numbers from normal distribution
arr2 = np.random.randn(3, 3)
# Random integers
arr3 = np.random.randint(10, 51, (4, 5))
# Print arrays
print("Random Numbers (0 to 1)")
print(arr1)
print("\n A 3x3 matrix of random numbers from standard normal distribution usingnp.random.randn()")
print(arr2)
print("\n A 2D array (4x5) of random integers between 10 and 50 using np.random.randint()")
print(arr3)