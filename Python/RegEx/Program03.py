# Find the numbers starting with 212 from a string

import re

regex = r"\b212\d*\b"
string = "212 Jeel-212Kite 21234 open0210"
match = re.findall(regex,string)

if match:
    print(match)