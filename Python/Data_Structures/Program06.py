# Convert any lower case string to upper case without in-built python functions.

string = input("Enter string to convert ")
list1 = []

for substring in string:
    if substring == " ":
        x = ord(substring)
    else:
        x = ord(substring) - 32
    list1.append(chr(x))

print(''.join(list1))



