# Write a NumPy program to compute the eigenvalues and eigenvectors of a given square array
import numpy as np

square_array = np.arange(1,10).reshape(3,3)
print("Square array is\n",square_array)

Eigen_value, Eigen_vector = np.linalg.eig(square_array)
print("Eigen value of given array is as follows\n",Eigen_value)
print("Eigen vectors of given array is as follows\n",Eigen_vector)