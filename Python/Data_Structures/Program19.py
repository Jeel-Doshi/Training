# Find the majority element of the given list.
#     Majority element: count of the element > N/2
#     N = length of list

input_list = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
length = int(len(input_list)/2)

occurence = {}

for element in input_list:
    if element in occurence:
        occurence[element] +=1
    else:
        occurence[element] = 1

if occurence[element] > length:
    print(element)
    
