lst=eval(input())
a=sum(lst)/len(lst)
b=a-int(a)
if b==0:
    print(int(a))
else:
    print("%.2f"%(a))
