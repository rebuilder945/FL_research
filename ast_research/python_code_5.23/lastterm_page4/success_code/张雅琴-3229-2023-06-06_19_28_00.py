a=[1,1,3,2,3,2]
b=[]
c=0
for x in a:
    if a.count(x)==1:
        b.append(str(x))
        c+=1
if c==0:
    print("False")
else:
    b.sort()
    print(",".join(b))
