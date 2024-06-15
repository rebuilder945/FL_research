ls = eval(input())
avg = sum(ls)/len(ls)
if avg % 1 == 0:
    print("%d"%(avg))
else:
    print("%.2f"%(avg))  
