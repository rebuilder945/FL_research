a=eval(input())
c=set(a)
b=[]
for x in c:
    if a.count(x)==1:
        b.append(a)
b.sort()
if b==[]:
    print("False")
else:
    c=list(map(str,b))
    print(",".join(c))
