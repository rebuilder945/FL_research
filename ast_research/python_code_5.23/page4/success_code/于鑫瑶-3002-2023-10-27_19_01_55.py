a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if float(d[1])==0:
    print(int(d))
else:
    print("%.2f"%d)
