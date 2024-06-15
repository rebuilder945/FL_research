l=eval(input())
l1=list(l)
a=sum(l1)/len(l1)
if sum(l1)%len(l1)==0:
    print("%d"%(a))
else:
    print("%.2f"%(a))
