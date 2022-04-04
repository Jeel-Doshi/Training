# Replace all special characters with space using regex

import re

string = 'Hello.. I am 21; years ^ old. My bday is $ in 11th month. Also % my fav number * is 3 and I like to work in 2:2:2 pattern with 1221256'

replaced = re.sub("\W", " ", string)
print(replaced)