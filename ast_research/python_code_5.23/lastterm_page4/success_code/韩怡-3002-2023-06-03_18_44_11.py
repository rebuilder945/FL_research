n=eval(input())
a=sum(n)/len(n)
b=int(a)
if type(b)==type(1):
    print("%d"%b)
else:
    print("%.2f"%a)

