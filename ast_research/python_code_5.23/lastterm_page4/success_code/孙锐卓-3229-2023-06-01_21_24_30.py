a=eval(input())
a.sort()
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
if b==[]:
    print(False)
else:
    c=','.join(str(i) for i in b)
    print(c)
 
