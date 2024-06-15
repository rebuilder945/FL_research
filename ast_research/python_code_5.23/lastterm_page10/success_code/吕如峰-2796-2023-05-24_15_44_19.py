import re

s = input()
l = re.findall(r'(\d*)', s)
res = sorted(l, key=lambda x: (x.isdigit(), len(x)),reverse=True )
print(res[0])
