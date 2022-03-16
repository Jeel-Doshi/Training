# Find the intersection (common) of two sets and remove those elements from the first set.

set1 = {1,2,5,4,3,6}
set2 = {4,5,8,9,6,1}

set_intersection = set1.intersection(set2)
print(set_intersection)

# Removed set
print(set1-set_intersection)

