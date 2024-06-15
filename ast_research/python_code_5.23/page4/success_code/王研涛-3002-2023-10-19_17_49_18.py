a=eval(input())
b=sum(a)/len(a)
c=b-int(b)
if c==0:
    print(int(b))
else:
    print("%.2f"%b)
