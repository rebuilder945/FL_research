list=list(eval(input()))
a=sum(list)
b=len(list)
c=a/b
c=float(c)
d=int(c)
if c-d<0.1:
    print(d)
else:
    print("%.2f"%c)

