lst = eval(input())
a = sum(lst)/len(lst)
if a %1==0:
    print("%d"%(a))
else:
    print("%.2f"%(a))
