# Find the majority element of the given list.
#     Majority element: count of the element > N/2
#     N = length of list

input_list = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
length = int(len(input_list)/2)


for element in input_list:
    counter = input_list.count(element)
    
    if counter > length:
        majority_element = element
        print(majority_element)
        break

