ls1 = eval(input())
a = sum(ls1)/len(ls1)
if a-int(a)==0:
    print("%.d"%a)
else:
    print("%.2f"%a)
