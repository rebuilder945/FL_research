from audioop import avg
ls1=eval(input())
c=sum(ls1)/len(ls1)
if c%1==0:
    print("%d"%c)
else:
    print("%.2f"%c)
