import numpy as np
try:
    # Ask user how many random numbers to generate
    n = int(input("Enter how many numbers you want to generate: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Generate random numbers between 10 and 100
        arr = np.random.randint(10, 101, n)
        print("\nGenerated Array")
        print(arr)
        # Display statistics
        print("\nMean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Minimum:", np.min(arr))
        print("Maximum:", np.max(arr))
        # Reshape only if possible
        if n % 2 == 0:
            matrix = arr.reshape(2, n // 2)
            print("\nReshaped 2D Array")
            print(matrix)
            print("\nRow-wise Sum")
            print(np.sum(matrix, axis=1))
        else:
            print("\nArray cannot be reshaped into a 2D matrix with 2 rows.")
except ValueError:
    print("Invalid input!")