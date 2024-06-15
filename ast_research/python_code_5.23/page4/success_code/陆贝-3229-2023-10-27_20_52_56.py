lt=eval(input())
ii=list()
ls=[]
for i in lt:
    a=lt.count(i)
    if a==1:
            ls.append(i)
if ls==[]:
    print("False")
else:
    ls.sort()
    s=""
    for i in ls:
        t=str(i)+","
        s=s+t
    print(s[0:-1])

