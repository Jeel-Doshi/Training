# Find the elements of the given list which are exactly the same as the entire product of the list except itself.

import math

input_list = [1, 5, 1, 10, 50]

#print(max(input_list))

for index in range(len(input_list)):
    store = input_list[index]
    input_list.remove(store)
    product = math.prod(input_list)

    if product == store:
        print(product)
        break
    else:
        input_list.insert(index,store)

