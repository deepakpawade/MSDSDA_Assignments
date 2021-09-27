# Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
x = np.array([1, 2, 3, 4])
print(np.all(x))


x = np.array([0, 1, 2, 3])
print(np.all(x))