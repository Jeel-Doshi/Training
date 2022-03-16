# Count the subsequence “AG” in the given string.

string = list(input("Enter string "))
sub_str = list(input("Enter substring to count "))

counter = 0
for i in sub_str:
    if i in string:
        counter += string.count(i)
        
print(counter)

