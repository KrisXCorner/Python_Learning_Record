import re

text = 'site sea sue sweet see case sse ssee loses'
match = re.findall(r"\bs\S*e\b",text)

if match:
    print(match)
else:
    print('not match')


number = '098439(028)329875174320232 4234578978275'
a = re.findall("\(?0\d{2,3}[) -]?\d{7,8}",number)
print(a)