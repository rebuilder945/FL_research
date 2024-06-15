a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if b%c:
    print("%.2f"%d)
else:
    print(int(d))
