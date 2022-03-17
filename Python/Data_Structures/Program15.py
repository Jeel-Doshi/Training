# Calculate the sum of the major and minor diagonals of the given matrix.

matrix = [ [2, 0, 7], [4, 1, 9], [8, 1, -1] ]
summation_minor = 0
summation_major = 0

for index1 in range(len(matrix)):
    for index2 in range(len(matrix)):
        if index1 == index2:
            summation_major += matrix[index1][index2]

        if index1 + index2 == len(matrix)-1:
            summation_minor += matrix[index1][index2]

print(summation_major)
print(summation_minor)


