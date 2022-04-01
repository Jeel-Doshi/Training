# Filter all elements that contain a sequence of lowercase alphabets followed by - followed by digits. They can be optionally surrounded by {{ and }}. Any partial match shouldn't be part of the output.
#    Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
#    Sample output: ['{{apple-150}}', 'grape-87']

# input_str = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']

# regex = ''

import re

mylist = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
r = re.compile(r"[a-z]+-\d+")
newlist = list(filter(r.match, mylist))
print(newlist)