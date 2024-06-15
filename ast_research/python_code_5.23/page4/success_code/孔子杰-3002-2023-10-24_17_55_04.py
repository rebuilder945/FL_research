lst=eval(input())
p=sum(lst)/len(lst)
if p==int(p):
    print("%d"%p)
else:
    print("%.2f"%p)
