# Write a NumPy program to compute the outer product of two given vectors
import numpy as np

vector1 = np.array([1,2,3,4,5])
print("First vector is\n",vector1)
vector2 = np.array([6,7,8,9,10])
print("Second vector is\n",vector2)

outer_product = np.outer(vector1,vector2)
print("The outer product of two vectors are as follows\n",outer_product)