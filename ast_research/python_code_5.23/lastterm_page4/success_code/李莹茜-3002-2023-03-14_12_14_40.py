biao=eval(input())
s=sum(biao)
l=len(biao)
a=s/l
if a-int(a)==0:
    a=str(a).rstrip("0")
    a=int(a.rstrip("."))
    print(a)
else:
    print("%.2f"%(a))
