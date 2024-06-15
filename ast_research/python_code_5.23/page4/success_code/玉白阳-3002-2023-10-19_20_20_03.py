ls1=input().split(",")
a=len(ls1)
b=sum(eval(ls1))
c=b/a
if c%1==0:
    print("%d"%c)
else:
    print("%.2f"%c)
