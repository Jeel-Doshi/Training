# Loop through the list and apply the regex to each element so that only items ending with a semicolon (;) are matched
import re

data = ['Ice cream;','Coffee','Shake;','Cocoa;','Fruit','Snow']
regex = r".*;$"

for element in data:
    match = re.search(regex,element)
    if match!= None:
        print(match.group())
    else:
        continue