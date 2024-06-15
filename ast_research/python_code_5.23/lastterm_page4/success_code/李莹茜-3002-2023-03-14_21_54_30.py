biao=eval(input())
s=sum(biao)
l=len(biao)
a=s/l
if a-int(a)==0:
   print("%d"%(a))
else:
    print("%.2f"%(a))
