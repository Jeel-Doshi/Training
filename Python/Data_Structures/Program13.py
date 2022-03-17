# Return the array which contains the elements that are greater than from its right side elements

# Method -1
input_array = [5, 17, 2, 6, 3]
output = []

output.append(input_array[-1])

for element in range(-2,-len(input_array)-1,-1):
    if input_array[element] > output[0]:
        output.insert(0,input_array[element])

print(output)

# Method -2
# for element in range(len(input_array)):
#     for next_elements in range(element+1,len(input_array)):
#         if input_array[element] < input_array[next_elements]:
#             break
#         else:
#             output.append(input_array[element])
#             break

# print(output + [input_array[-1]])

