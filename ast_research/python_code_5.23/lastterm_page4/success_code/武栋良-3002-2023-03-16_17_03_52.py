ls = eval(input())
a = sum(ls)/len(ls)
b = int(a)
if a==b:
    print(a)
else:
    print("%.2f"%(a))
