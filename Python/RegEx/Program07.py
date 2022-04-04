# Replace the space character that occurs after a word ending with a or r with a newline character
#       Sample input: area, not an _a2_ roar took 22
#       Sample output:
#       area
#       not a
#       _a2_ roar
#       took 22

import re

input_str = 'area not an _a2_ roar took 22'
replace = re.findall(r"\b[A-Za-z]*a\b|\b[A-Za-z]*r\b", input_str)
split_str = input_str.split(" ")
result = ' '

for element in split_str:
    result = result + element + " " 
    if element in replace:
        result = result + "\n" 
   
print(result) 