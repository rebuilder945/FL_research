a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print("False")
else:
    b.sort()
    for i in b:
        b[i]=str(b[i])
    print(",".join(b))


