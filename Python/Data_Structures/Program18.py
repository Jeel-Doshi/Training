# Find maximum sum of triplets in an array such than i < j < k and a[i] < a[j] < a[k]

input_list = [2, 5, 3, 1, 4, 9]
result = []

index = 0
for index1 in range(len(input_list)):
    for index2 in range(index1+1,len(input_list)):
        if (index < index1 < index2) and (input_list[index] < input_list[index1] < input_list[index2]):
            
                addition = input_list[index] + input_list[index1] + input_list[index2]
                result.append(addition)
                
else:
    index+=1

print(max(result))

