a= eval(input())
b=sum(a)
c=len(a)
d=b/c
e=str(d).split('.')[1]
if e==0:
    print(int(d))
if e!=0:
    print("%.2f"%(d))
