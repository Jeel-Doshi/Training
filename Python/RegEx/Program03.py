# Find the numbers starting with 212 from a string
import re

regex = r"^212.*"

string = "212 3421 231 22134 5 2 212 3 221 21256 21287"
splited_string = string.split()

for i in splited_string:
    match = re.search(regex,i)
    if match != None:
        print(match[0])
    else:
        continue

# Done - check