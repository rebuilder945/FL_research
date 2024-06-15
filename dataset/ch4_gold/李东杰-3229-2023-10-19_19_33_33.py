a=eval(input())
c=[]
s=""
for x in a:
    b=a.count(x)
    if b==1:
        c.append(x)
    else:
        continue
if len(c)==0:
    print("False")
else:
    c.sort()
    for x in c:
        s=s+str(x)+","
    print(s)

