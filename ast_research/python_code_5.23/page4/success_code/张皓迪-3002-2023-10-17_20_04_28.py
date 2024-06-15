ls=eval(input())
a=sum(ls)/len(ls)
if a%1==0:
    a=int(a)
    print(a)
else:
    print("%.2f"%(a))

