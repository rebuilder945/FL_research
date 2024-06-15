a=eval(input())
ii=[]
for i in a:
    c=a.count(i)
    if c==1:
        i=str(i)
        ii.append(i)
if ii==[]:
    print("False")
else:
    s=""
    for x in ii:
        x=x+","
        s=s+x
    z=s[:-1]
    print(z)
