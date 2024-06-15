ls=eval(input())
ls2=set(ls)
c=[]
for i in ls2:
    if ls.count(i)==1:
        c.append(i)
c.sort()
if c:
    print(",".join(str(i for i in c)))
else:
    print("False")
