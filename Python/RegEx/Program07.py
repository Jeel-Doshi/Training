# Replace the space character that occurs after a word ending with a or r with a newline character
#       Sample input: area, not an _a2_ roar took 22
#       Sample output:
#       area
#       not a
#       _a2_ roar
#       took 22

import re

input_str = 'area, not an _a2_ roar took 22'

replaced = re.sub(r"(a|r)\b", "\n", input_str)
print(replaced)
