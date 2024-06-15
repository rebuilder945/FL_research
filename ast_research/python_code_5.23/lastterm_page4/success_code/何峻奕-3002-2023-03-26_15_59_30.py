a=eval(input())
b=sum(a)%len(a)
c=sum(a)/len(a)
if b==0:
    d=int(c)
    print(d)
if b!=0:
    print("%.2f"%c)

