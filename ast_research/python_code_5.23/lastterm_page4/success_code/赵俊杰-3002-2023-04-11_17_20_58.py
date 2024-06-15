ls=eval(input())
a=sum(ls)/len(ls)
b=round(a)
if a-b==0:
    print(b)
else:
    print("%.2f"%(a))

