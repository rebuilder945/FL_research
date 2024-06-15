a=eval(input())
b=[]
c=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print("False")
else:
    b.sort()
    for i in b:
        i=str(i)
        c.append(i)
    print(",".join(c))

