ls1=eval(input())
s=sum(ls1)/len(ls1)
if sum(ls1)%len(ls1)==0:
    print("%d"%s)
else:
    print("%.2f"%s)
