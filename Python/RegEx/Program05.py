# Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign

import re

regex = r"^([a-z0-9_\.-]+@)"
email = "movie.32@gmail.com"
# email = "tome12@gmail.com"
# email = "kite_fly@gmail.com"

match = re.findall(regex,email)
print(match)