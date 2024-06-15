ls = eval(input())
a = sum(ls)/len(ls)
b = a - int(a)
if b == 0 :
    print(int(a))
else:
    print("%.2f"%(a))
