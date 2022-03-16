# Return the array which contains the elements that are greater than from its right side elements

input_array = [5, 17, 2, 6, 3]
output = []

for elements in range(len(input_array)):
    for next_elements in range(elements+1,len(input_array)):
        if input_array[elements] < input_array[next_elements]:
            break
        else:
            output.append(input_array[elements])
            break

print(output + [input_array[-1]])

# [3, 14, 3, 7, 2]
# [14, 7, 2]

