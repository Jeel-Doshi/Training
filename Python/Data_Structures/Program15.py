# Calculate the sum of the major and minor diagonals of the given matrix.

matrix = [ [2, 0, 7], [4, 1, 9], [8, 1, -1] ]
sum_minor = 0
sum_major = 0

for index in range(len(matrix)):

    sum_major += matrix[index][index]
    sum_minor += matrix[index][len(matrix)-1-index]

print(sum_major)
print(sum_minor)


# Done