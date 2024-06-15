a=input()
b=[]
c=[]
for i in a:
    if i.isdigit():
        b.append(i)
        if len(b)>=len(c):
            c=b.copy()
    else:
        b=[]
if len(c)>0:
    print(''.join(c))
else:
    print('No digits')
