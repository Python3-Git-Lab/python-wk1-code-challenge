import string
from itertools import groupby

# #Printed the alphabets
lower = list(string.ascii_lowercase)  #Alphabets
my_dict = {item: index + 1 for index, item in enumerate(lower)} #Dictionary for alphabet as value and index as the key


def solve(s):
    vowels = "aeiou"
    consonant_substrings = ["".join(g) for k, g in groupby(s, key=lambda x: x in vowels) if not k]

    max_value = 0
    for substring in consonant_substrings:
        value = sum(ord(c) - ord('a') + 1 for c in substring)
        max_value = max(max_value, value)

    return max_value

print(solve("zodiacs"))  
print(solve("strength"))
print(solve("munuhe"))  




        

