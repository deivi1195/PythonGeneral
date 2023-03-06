import re

text = "the quick browwn fox jumps over the lazy dog"

x = re.search("^the.*dog$",text)

if x:
    print("SI")
else:
    print("NO")


















