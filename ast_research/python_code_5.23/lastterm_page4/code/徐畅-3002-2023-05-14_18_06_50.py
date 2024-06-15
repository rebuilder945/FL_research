lst=eval(input())
a=sum(lst)/len(lst)
if a-int(a)==0:
    print(int(a)):
else:
    print("%.2f"%a)
