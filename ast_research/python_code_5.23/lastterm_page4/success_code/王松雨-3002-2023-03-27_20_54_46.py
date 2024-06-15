lst=eval(input())
a=sum(x for x in lst)/len(lst)
if a-int(a)==0:
    print("%.d"%a)
else:
    print("%.2f"%a)
