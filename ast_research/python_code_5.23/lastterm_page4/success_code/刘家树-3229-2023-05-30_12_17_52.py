l=eval(input())
ll=list(set(l.copy()))
for x1 in ll:
    a=l.count(x1)
    if l.count(x1)>1:
        while a>0:
            l.remove(x1)
            a-=1
l.sort()
if l==[]:
    print("False")
else:
    print(",".join(l))


