# Add 1 to the given list of elements. Do not use string conversion, number conversion.

input_array = [1,9,9,9]
number = 0

for elements in range(len(input_array)):
    number = number *10 + input_array[elements]

# adding one
addition = number + 1

added_list = []

while addition > 0:
    digits = addition % 10
    added_list.append(digits)
    addition = addition // 10

print(added_list[::-1])  


