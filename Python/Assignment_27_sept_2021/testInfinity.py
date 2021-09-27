# Write a NumPy program to test element-wise for positive or negative infinity.
import numpy as np, math
a = np.array([1, 0,math.inf, -math.inf, float('inf'), float('-inf')])
print(np.isinf(a))