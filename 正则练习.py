import re

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))


# pattern = re.compile(r'(Na){0,3}')

# result = pattern.search('NaNaNa')
# print(result.group(1))

# greedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())

import pyperclip

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4}) # dot-s  omething
)''', re.VERBOSE) 

text = str(pyperclip.paste())
match = []

for groups in emailRegex.findall(text):
    match.append(groups[0])
  # Copy results to the clipboard.
if len(match) > 0:
    pyperclip.copy('\n'.join(match))
    print('Copied to clipboard:')
    print('\n'.join(match))
 
