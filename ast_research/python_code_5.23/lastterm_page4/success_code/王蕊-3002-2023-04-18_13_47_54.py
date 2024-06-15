a=eval(input())
b=len(a)
c=0
for x in a:
   c+=x
d=c//b
e=d-int(d)
if e==0:
    print(int(d))
elif e!=0:
    print("%.2f"%d)

