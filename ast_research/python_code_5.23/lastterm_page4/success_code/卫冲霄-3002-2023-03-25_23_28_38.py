ls=eval(input())
a=sum(ls)/len(ls)
if a-int(a)==0:
    print(int(a))
else:
    print("%.2f"%(a))
