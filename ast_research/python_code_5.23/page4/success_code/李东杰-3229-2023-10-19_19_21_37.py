a=eval(input())
c=[]
s=""
for x in a:
    b=a.count(x)
    if b==1:
        c.append(x)
        c.sort()
        s=s+str(c)
    else:
        continue
if len(c)==0:
    print("False")
else:
    print(s)

