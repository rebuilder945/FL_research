ls=eval(input())
s=""
ii=[]
for i in ls:
    s=s+i
for i in s:
    ii.append(i)
ii.sort()
oo=[]
for x in ii:
    c=ii.count(x)
    s=str(c)
    z=x+","+s
    if z not in oo:
        oo.append(z)
#print(oo)
for t in oo:
    print(t)


    

    

