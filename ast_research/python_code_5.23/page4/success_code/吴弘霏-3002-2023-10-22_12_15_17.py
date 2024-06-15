list=eval(input())
a=sum(list)%len(list)
if a==0:
    print("%d"%a)
else:
    print("%.2f"%a)

