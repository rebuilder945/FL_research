a=eval(input())
b=0
c=0
for x in a:
    b=b+x
    c=c+1
d=b/c
e=int(d)
if d-e==0:
    print(d)
else:
    print("%.2f"%d)
