a=input()
print(a)
b=''
c=''
for i in a:
    if i.isdigit():
        b+=i
    else:
        if len(c)<=len(b):
            c=b
            b=''
if len(c)<=len(b):
            c=b
if len(c)>0:
    print(c)
else:
    print('No digits')
