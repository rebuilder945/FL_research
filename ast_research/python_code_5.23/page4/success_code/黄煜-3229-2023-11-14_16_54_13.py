a=eval(input())
c=[]
d=1
for i in a:
    b=a.count(i)
    if b==1:
        c.append(i)
        d=0
c.sort()
c=','.join(str(i) for i in c)
if d==0:
    print(c)
else:
    print("False")


