lst=eval(input())
a=sum(lst)/len(lst)
if a==int(a):
    print(int(a))
if not a==int(a):
    print("%.2f"%a)



