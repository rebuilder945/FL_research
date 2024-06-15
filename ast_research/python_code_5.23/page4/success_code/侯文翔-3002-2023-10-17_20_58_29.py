ls=eval(input())
b=sum(ls)/len(ls)
if b%1!=0:
    print("%.2f"%b)
else:
    print(b)
