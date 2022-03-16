# Find the max sum of subarray

input_list = [-2, -3, 4, -1, -2, 1, 5, -3]

list1 = []
for i in range(len(input_list)):
    for j in range(i+1,len(input_list)):
        list2 = input_list[i:j]
        list1.append(sum(list2))

print(max(list1))  

