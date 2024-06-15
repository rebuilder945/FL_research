ls1 = eval(input())
a = sum(ls1)/len(ls1)
if isinstance(a,int):
    print(a)
else:
    print("%.2f"%a)


