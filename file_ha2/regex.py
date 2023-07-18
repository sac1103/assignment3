"to display the given string using regex"
import re
STR1 = "sachin,sanjay,manoj,sanoj"

 # Find words that start with "sa"
result1 = re.findall(r"\bsa\w*\b", STR1)
print(result1)


# Matches words starting with "s" and ending with in
result2 = re.findall(r"\bs\w*in\b", STR1)
print(result2)


# Matches any word that ends with "oj"
result3 = re.findall(r"\w*oj\b", STR1)
print(result3)
