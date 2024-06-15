lst=eval(input())
a=sum(lst)/len(lst)
if type(a)==int:
    print(int(a))
else:
    print("%.2f"%(a))
