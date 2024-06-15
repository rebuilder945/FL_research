ls=eval(input())
a=sum(ls)/len(ls)
if int(a)-a==0:
    a=int(a)
    print(a)
else:
    a=float(a)
    print("%.2f"%(a))    

