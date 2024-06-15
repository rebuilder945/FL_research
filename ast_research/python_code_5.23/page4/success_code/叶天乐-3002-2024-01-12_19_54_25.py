ls1 = eval(input())
a = sum(ls1)/len(ls1)
if a/round(a) == 1:
    print(int(a))
else:
    print("%.2f"%a)
