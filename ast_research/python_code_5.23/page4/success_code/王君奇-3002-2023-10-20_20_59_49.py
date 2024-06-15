a=eval(input())
b=sum(a)
c=b/len(a)
d=b//len(a)
e=b%len(a)
if e==0:
    print(d)
else:
    print("%.2f"%c)
