a=eval(input())
b=sum(a)
c=len(a)
d=b%c
if d==0:
    print(b/c)
else:
    print("%.2f"%(b/c))
