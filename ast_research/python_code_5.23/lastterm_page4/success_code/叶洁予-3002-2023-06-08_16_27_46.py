lst=eval(input())
a=sum(lst)/len(lst)
a_int=int(a)
if a_int >a:
    print("%.2f"%a)
else:
    print(a_int)
