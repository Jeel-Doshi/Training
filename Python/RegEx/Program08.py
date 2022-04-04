# Split the given input string on one or more repeated sequences of a cat using regex
#     Sample input: firecatlioncatcatcatbearcatcatparrot
#     Sample output: ['fire', 'lion', 'bear', 'parrot']

import re

input_str = 'firecatlioncatcatcatbearcatcatparrot'

result = re.split(r'(?:cat)+',input_str)
print(result)