# Count the occurrence of each element from a lelementst 

array = [1,2,3,4,5,6,2,3,1]

output = {}

for element in array:
    if element in output:
        output[element] +=1
    else:
        output[element] = 1

print(output)

# Method -2
# for element in array:
#     counter = a.count(element)
#     output[element] = counter

# print(output)