# Write a NumPy program to compute the determinant of a given square array
import numpy as np

square_array = np.arange(1,10).reshape(3,3)
print("Square array is\n",square_array)

determinant = np.linalg.det(square_array)
print("Determinant of square array is as follows\n",determinant)