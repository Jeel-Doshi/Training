# Write a regular expression to search digits inside a string

import re

regex = r"[0-9]+"

string = "Hello..I am 21 years old. My bday is in 11th month. Also my fav number is 3 and I like to work in 2:2:2 pattern"

match = re.findall(regex,string)
print(match)

# Done