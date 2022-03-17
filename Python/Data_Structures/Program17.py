# Print reverse string using recursion.

input_str = input("Enter string to reverse ")
length = len(input_str)

# def rev(string):
    
#     if len(string) == 0:
#         return rev(string)
#     else:
#         print(string[len(string)-1])
        
#         return string[len(string)-1] + rev(string[length])

# print(rev(input_str))

def rev(string):
    
    string[length-1]

    length -= 1
    return rev(string[length])

print(rev(input_str))

