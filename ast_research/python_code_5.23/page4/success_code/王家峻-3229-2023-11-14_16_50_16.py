n=eval(input())
c=[]
for x in n:
    if n.count(x)==1:
        c.append(x)
        c.sort()
if c==[]:
    print('False')
else:
    c=list(map(str,c))
    for x in c:
        b=','.join(c)
    print(b)
    

