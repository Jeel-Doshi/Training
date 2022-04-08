# Write a NumPy program to compute the cross-product of two given vectors
import numpy as np

vector1 = np.array([1,2,3])
print("First vector is\n",vector1)
vector2 = np.array([4,5,6])
print("Second vector is\n",vector2)

cross_prod = np.cross(vector1,vector2)
print("Cross-Product of two vectos is as follows\n",cross_prod)