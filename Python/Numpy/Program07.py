# Write a NumPy program to compute the sum of the diagonal elements of a given array

import numpy as np

array = np.array([[4, 9, -6], [15, -14, 3], [9, -2, 0]])
print("Given array is\n",array)

sum_diag = np.trace(array)
print("Sum of diagonal element of given array is\n",sum_diag)