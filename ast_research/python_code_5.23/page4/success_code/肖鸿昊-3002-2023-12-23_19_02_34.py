a=eval(input())
s=sum(a)/len(a)
if s%1==0:
    print("%d"%(s))
else:
    print("%.2f"%(s))
