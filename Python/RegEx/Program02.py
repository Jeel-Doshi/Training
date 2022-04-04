# Find the words with exactly 8 letters from a paragraph using regex

import  re

para = "The phrase regular expressions, or regexes, is often used to mean the specific, standard textual syntax for representing patterns for matching text, as distinct from the mathematical notation described below. Each character in a regular expression (that is, each character in the string describing its pattern) is either a metacharacter, having a special meaning, or a regular character that has a literal meaning. For example, in the regex b., 'b' is a literal character that matches just 'b', while '.' is a metacharacter that matches every character except a newline"

check = re.findall(r"\b[A-Za-z]{8}\b",para)
print(check)