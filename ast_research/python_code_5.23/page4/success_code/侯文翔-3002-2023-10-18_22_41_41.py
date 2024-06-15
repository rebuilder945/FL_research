ls=eval(input())
a=sum(ls)/len(ls)
if a%1!=0:
    print("%.2f"%a)
else:
    b=int(a)
    print(b)
