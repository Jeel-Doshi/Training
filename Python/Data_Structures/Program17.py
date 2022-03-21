# Print reverse string using recursion.

input_str = input("Enter string to reverse ")
length = len(input_str)

def rev(string,last_index):
    
    last_index -= 1

    if last_index == 0:
        return string[last_index]
        
    return string[last_index] + rev(string,last_index)

print(rev(input_str,length))