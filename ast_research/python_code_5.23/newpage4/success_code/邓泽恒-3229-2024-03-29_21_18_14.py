n=eval(input())
a=[]
for x in n:
    if n.count(x)==1:
        a.append(x)
a.sort()
if len(a)==0:
    print(False)
else:
    s=','.join(map(str,a))
    print(s)
