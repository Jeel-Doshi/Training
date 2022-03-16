# Slice list into 3 equal chunks and reverse each chunk
 
Sample = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Method -1
chunk1 = Sample[:3]
chunk2 = Sample[3:6]
chunk3 = Sample[6:]

list1 = [chunk1,chunk2,chunk3]
list2 = []

for value in list1:
    value = value[::-1]
    list2.append(value)

print(list2)


# Method -2
# list1 = [1,2,3,4,5,6,7]
# value = 0
# list3 = []

# while value < len(list1):
#     list2 = list1[value:value+3]
#     list3.append(list2[::-1])
#     value+=3

# print(list3)               
