ls=eval(input())
a=sum(ls)/len(ls)
if a%1==0:
    print(int(a))
else:
    print("%.2f"%a)
