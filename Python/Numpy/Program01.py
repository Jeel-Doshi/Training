# Write a NumPy program to compute the multiplication of two given matrices
import numpy as np

matrix1 = np.arange(1,7).reshape(2,3)
print("First matrix is\n",matrix1)
matrix2 = np.arange(1,7).reshape(3,2)
print("Second matrix is\n",matrix2)

multiplication = matrix1.dot(matrix2)
print('Multiplication of two matrices are as follows\n',multiplication)