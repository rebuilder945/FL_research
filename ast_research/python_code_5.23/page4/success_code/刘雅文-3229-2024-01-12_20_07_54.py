a=eval(input())
c=[]
for x in a:
    b=a.count(x)
    if b==1:
        c.append(x)
if len(c)>0:
    c.sort()
    print(','.join(map(str,c)))
else:
    print('False')
