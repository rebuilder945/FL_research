a=eval(input())
b=[]
for x in a[:]:
    if a.count(x)==1:
        b.append(x)
if b.count(x)>0:
    b.sort()
    c=','.join(map(str,b))
    print(c)
else:
    print("False")
