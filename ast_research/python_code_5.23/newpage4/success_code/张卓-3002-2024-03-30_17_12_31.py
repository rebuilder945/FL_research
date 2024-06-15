a=list(eval(input()))
b=sum(a)/len(a)
c=b-int(b)
if c==0:
    print(b)
elif c!=0:
    print("%.2f"%b)
