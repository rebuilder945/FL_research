a=eval(input())
b=sum(a)/len(a)
c="%.2f"%b
if int(b)-float(c)==0:
    print(int(b))
else:
    print(c)
