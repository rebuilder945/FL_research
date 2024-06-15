from audioop import avg
lst=eval(input())
original=sum(lst)/len(lst)
if original>avg:
    print("%.2f"%(original))
else:
    print("%.2f"%(avg))
