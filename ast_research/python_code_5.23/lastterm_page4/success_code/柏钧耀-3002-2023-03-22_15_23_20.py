a=eval(input())
b=sum(a)/len(a)
if b%1==0:
    print("%.0f"%(b))
else:print("%.2f"%(b))

