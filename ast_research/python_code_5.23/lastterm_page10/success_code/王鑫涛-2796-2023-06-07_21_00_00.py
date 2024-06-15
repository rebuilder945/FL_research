a=input()
m=''
x=''
for i in a:
    if i in list('0123456789'):
        m+=i
        if len(m) > len(x):
            x=m
    else:
        m=''
if not x:
    print(x)
else:
    print('No digits')
