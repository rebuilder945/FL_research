lst=eval(input())
a=sum(lst)/len(lst)
if type(a)==int:
    print("%.0f"%(a))
else:
    print("%.2f"%(a))
