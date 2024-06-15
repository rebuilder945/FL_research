n=eval(input())
a=sum(n)/len(n)
b=int(a)
if type(a)==type(1):
    print("%d"%b)
else:
    print("%.2f"%a)

