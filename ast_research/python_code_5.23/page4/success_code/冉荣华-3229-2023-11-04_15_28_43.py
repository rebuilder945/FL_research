x=eval(input())
a=[]
for i in x :
    if x.count(i)==1:
        a.append(i)
if len(a)>=1:
    a.sort()
    a=','.join(str(i) for i in a)
    print(a)
else:
    print(False)
