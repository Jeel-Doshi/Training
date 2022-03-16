# Create a function to reverse the entire list without any function and also do not use any slicing shortcut.

def rev():
    input_list = list(map(int, input("Enter multiple values: ").split()))
    list1 = []

    for index in range(-1,-len(input_list)-1,-1):
        list1.append(input_list[index])    

    return list1

print(rev())

# To reverse list itself
# def rev():
#     list1 = [1,2,3,8,5,6]
#     for start in range(int(len(list1)/2)):
#         end = len(list1)-start-1
#         list1[start],list1[end] = list1[end],list1[start]
#         end-=1
#     return list1
# print(rev())


# Method -3
# def rev():
#     input_list = [1,2,3,4,5]
#     list1 = []
#     for index in range(len(input_list)):
#         x = input_list.pop()
#         list1.append(x)
#     return list1
# print(rev())