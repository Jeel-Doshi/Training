# Return product of minimum of odd and maximum of even from a given list. do not use in-built min/max function.

input_array = [7, 5, 2, 3, 12, 9, 15, 24]

even_list = list(filter (lambda x: x % 2 == 0, input_array))
odd_list = list(filter (lambda x: x % 2 != 0, input_array))

max_even = even_list[0]
for i in even_list:
    if max_even < i:
        max_even = i

min_odd = odd_list[0]
for i in odd_list:
    if min_odd > i:
        min_odd = i

print(max_even*min_odd)

