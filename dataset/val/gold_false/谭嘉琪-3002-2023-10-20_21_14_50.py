a=eval(input())
b=0
for i in a:
    b=b+i
c=len(a)
d=b//c
e=d-int(d)
if e==0:
    print(int(d))
else:
    print("%f.2"%(d))
