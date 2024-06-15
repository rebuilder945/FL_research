lst = eval(input())
avg = sum(lst)/len(lst)
if avg % 1 ==0:
    print("%.0f"%(avg))
else:
    print("%.2f"%(avg))
