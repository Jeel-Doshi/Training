# Write a NumPy program to compute the inverse of a given matrix
import numpy as np

matrix = np.array([[-12, 4, 2], [1, -7, 6], [-9, 0, 5]])
print("Given matrix is\n",matrix)

inverse_matrix = np.linalg.inv(matrix)
print("Inverse of given matrix is as follows\n",inverse_matrix)