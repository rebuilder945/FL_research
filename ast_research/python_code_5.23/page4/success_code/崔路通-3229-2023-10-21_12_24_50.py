a=eval(input())
b=a.copy()
c=[]
d=""
for x in b:
    if a.count(x)==1:
        c.append(x)
        c.sort()
if not c:
    print("False")
else:
    for x in c[0:-1]:
        x=str(x)
        d=d+x+","
    d=d+str(c[-1])
    print(d)
        

   
