a=eval(input())
x=sum(a)%len(a)
if x==0:
    h=sum(a)/len(a)
    print(h)
else:
    h=sum(a)/len(a)
    print("%.2f"%(h))

