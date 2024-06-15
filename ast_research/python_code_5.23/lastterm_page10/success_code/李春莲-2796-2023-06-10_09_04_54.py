import re
s=input()
l=re.findall('\\d+', s)
if l:
    n=l[0]
    for i in l:
        if len(i)>=len(n):
            n=i
    print(n)
else:
    print('No digits')
