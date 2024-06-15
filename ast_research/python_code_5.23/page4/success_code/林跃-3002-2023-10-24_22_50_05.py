lst=eval(input())
if sum(lst)/len(lst)==0:
    print(int(sum(lst)/len(lst)))
else:
    print("%.2f"%(sum(lst)/len(lst)))
