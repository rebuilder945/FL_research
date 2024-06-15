a=eval(input())
b=sum(a)
e=b/len(a)
c=b%len(a)
if c!=0:
    print("%.2f"%e)
else:
    print("%d"%e)
