a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
c=[]
if b==[]:
    print("False")
else:
    b.sort()
    for i in b:
        c.append(str(i))
    print(','.join(c))


