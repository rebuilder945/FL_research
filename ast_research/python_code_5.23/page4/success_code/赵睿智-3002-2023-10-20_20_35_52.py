lst=eval(input())
x=sum(lst)/len(lst)
if x-int(x)==0:
    print("%d"%x)
else:
    print("%.2f"%x)

