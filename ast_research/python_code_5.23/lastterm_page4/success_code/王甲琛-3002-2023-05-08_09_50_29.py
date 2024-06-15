lst=eval(input())
a=sum(lst)/len(lst)
if a-int(a)!=0:
    print("%.2f"%a)
else:
    print(int(a))
