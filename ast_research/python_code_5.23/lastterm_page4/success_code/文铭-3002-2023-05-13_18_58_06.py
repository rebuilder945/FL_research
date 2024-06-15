ls = eval(input())
ag = sum(ls)/len(ls)
f  = ag-int(ag)
if f == 0:
    print(int(ag))
else:
    print("%.2f"%ag)
