# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

input_array = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(li_tup):
    return li_tup[1]

def sorting(a):
    return sorted(a,key=last)

print(sorting(input_array))

