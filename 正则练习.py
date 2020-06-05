import re

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))


# pattern = re.compile(r'(Na){0,3}')

# result = pattern.search('NaNaNa')
# print(result.group(1))

greedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())