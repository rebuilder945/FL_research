a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if len(b)==0:
    print(False)
else:
    b.sort()
    c=""
    for i in b:
            c=c+","+str(i)
    print(c[1::])
