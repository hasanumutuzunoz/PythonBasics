import re
str = "take up 1-3-2019 oneasdas23das idea, 6749 Oneaasssdd idea at 99 a ti897294728374me One 12-11-2020"

# r for regular expression
# o is the letter we are searching
# \w\w for adding to search any alfa numeric character -> Capital letter, non capital letter, any number from 0 to 9
# str is for string we want to search

"""
\w any alfa numeric value (any digit or character)
\W non-alfa numeric character
\d digit
\D non-digit
\s white space
\S non-white sapce
\b space around words
\A ssearch at the beginning of the string 
\Z seacrh only at the end of the string 
"""

"""
+ 1 or more  (\d+ find 1 or more digits)
* 0 or more 
? 0 or 1
{m} m times
{m,n} min m, max n times
"""

# Search returns one result
result = re.search(r'o\w\w\w\w\w', str)
# .group give us the exact string we are searching
print(result.group())

# Findall starts from the beginning and all the way to ethe end returns list of all findings
result = re.findall(r'o\w\w', str)
print(result)

# Math searches only at the beginning of the giving string
result = re.match(r't\w\w', str)
print(result.group())

# /d is for digit
# Split whenever there is a digit in the string
# + is for 1 or more
result = re.split(r'\d+', str)
print(result)

# Subsitute (Change) strings
result = re.sub(r'one','two', str)
print(result)

# Find all characters after O
result = re.findall(r'O\w+', str)
print(result)

# Find 0 or more characters after O
result = re.findall(r'O\w*', str)
print(result)

# Find 0 or 1 characters
result = re.findall(r'O\w?', str)
print(result)

# Find 4 characters after O
result = re.findall(r'O\w{4}', str)
print(result)

# Find min 1 max 4 after O
result = re.findall(r'O\w{1,4}', str)
print(result)

# (FIND DATES) Find min 1 max 2 digits, Find min 1 max 2 digits, Find 4 digits
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

# ^ is for searching at the beginning of the string
result = re.search(r'^t\w', str)
print(result.group())

# find at the beginning, start with t, and any number of character after t
result = re.search(r'^t\w*', str)
print(result.group())

