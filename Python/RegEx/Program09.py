# Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits. They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.
#    Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
#    Sample output: ['{{apple-150}}', 'grape-87']

import re

input_str = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
regex = r"{+[a-z]+-[0-9]+}+|([a-z]+-[0-9]+)"
result = []

for element in input_str:
    match = re.match(regex,element)
    if match:
        result.append(match.group())
print(result)