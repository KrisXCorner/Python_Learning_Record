import re

text = "aAsmr3idd4bgs7Dlsf9eAF"

n = "".join(re.findall(r'\d',text))
print(n)