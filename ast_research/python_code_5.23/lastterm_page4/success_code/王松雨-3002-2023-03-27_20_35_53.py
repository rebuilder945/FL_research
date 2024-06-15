lst=eval(input())
a=sum(lst)/len(lst)
if a is int:
    print(a)
elif a is float:
    print("%.2f"%a)
