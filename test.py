
# Program to extract numbers from a string

import re

string = 'hello 132 hi 89. Howdy 34'
pattern = '\d\d\d'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']
