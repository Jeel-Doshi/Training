# Return the sum of duplicates elements from the given List

input_list = [3, 5, 6, 11, 12, 3, 5, 2]
duplicate = []

for value in input_list:
    count = input_list.count(value)
    if count>1:
        input_list.append(value)

print(sum(set(duplicate)))

