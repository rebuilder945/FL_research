a=input()
d=''
c=''
for i in a:
    if i.isdigit():
        d+=i
        if len(d)>=len(c):
            c=d
    else:
        d=''
if len(c)>0:
    print(c)
else:
    print('No digits')

