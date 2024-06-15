lst=eval(input())
a=sum(lst)/len(lst)
b=int(a)
if b==a:
    print(b)
else:
    print("%.2f"%a)
