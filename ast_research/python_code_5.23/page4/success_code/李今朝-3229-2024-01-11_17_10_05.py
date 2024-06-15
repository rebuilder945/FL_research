a=eval(input())
b=[]
for x in range(len(a)):
    if a.count(x)==1:
        b.append(x)
if len(b)>0:
    b.sort()
    print=','.join( str(i) for i in b)
else:
    print('False')
