import os
import codecs

chinese_char_path = '../data/char_set.txt'

'''
with open(chinese_char_path, "rb") as f:
    lines = f.readlines()

chars = []
for line in lines:
    line = line.decode("utf-8")
    chars.append(line[0])

str = "".join(("".join(chars)).split())
print(str)

with codecs.open(os.path.join(os.path.dirname(chinese_char_path), "char_string.txt"), 'w', 'utf-8') as f:
    f.write(str)

'''

with codecs.open(chinese_char_path, encoding='utf-8') as f:
    content = f.read()
    print("".join(content.split()))
    print(type(content))
