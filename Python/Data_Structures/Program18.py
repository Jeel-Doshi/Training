# Find maximum sum of triplets in an array such than i < j < k and a[i] < a[j] < a[k]

input_list = [2, 5, 3, 1, 4, 9]
result = []

for index1 in range(len(input_list)):
    for index2 in range(index1+1,len(input_list)):
        for index3 in range(index1+2,len(input_list)):
            if index1 < index2 < index3 :
                if input_list[index1] < input_list[index2] < input_list[index3]:
                    summation = input_list[index1] + input_list[index2] + input_list[index3]
                    result.append(summation)

print(max(result))

