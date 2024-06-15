lst=eval(input())
s=sum(lst)/len(lst)
t=s*10
if t%10==0:
    print(int(s))
else:
    print("%.2f"%s)
