# Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np
x = np.array([1, 0, 0, 0])
print(np.any(x))
x = np.array([0, 0, 0, 0])
print(np.any(x))