n=eval(input())
a=sum(n)/len(n)
if type(a)==type(1.1):
    print("%.2f"%a)
else:
    print("%d"%a)

