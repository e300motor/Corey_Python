import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

print('\tTab')
print(r'\tTab')         #raw string handled by regular expressions , not python

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
print(text_to_search[1:4])

# p = re.compile(r'coreyms\.com', re.IGNORECASE)  # match='coreyms.com'
# p = re.compile(r'\d{3}[-.]\d{3}[-.]\d{3}')  #[.] match . only not any character
# p = re.compile(r'[1-5]')           # 1 or 2 or 3 or 4 or 5
p = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
m = p.finditer(text_to_search)
for i in m:
    print(i)


# pattern = re.compile(r'start', re.I)   # re.I = re.IGNORECASE

# matches = pattern.search(sentence)

# print(matches)
