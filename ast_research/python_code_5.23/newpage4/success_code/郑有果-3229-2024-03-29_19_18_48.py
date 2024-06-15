m=eval(input())
n=[]
for x in m:
    if m.count(x)==1:
        n.append(x)
n.sort()
if n:
    print(",".join(str(i)for i in n))
else:
    print("False")

