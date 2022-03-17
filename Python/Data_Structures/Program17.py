# Print reverse string using recursion.

input_str_list = list(input("Enter string to reverse "))

def last_element(list1):
    return list1[-1]

while len(input_str_list) > 0:
    reversed_str = []
    lastElement = last_element(input_str_list)
    input_str_list.pop()
    reversed_str.append(lastElement)

    print(''.join(reversed_str),end='')

