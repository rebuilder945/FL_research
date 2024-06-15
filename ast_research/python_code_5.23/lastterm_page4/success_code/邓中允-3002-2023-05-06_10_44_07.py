a=eval(input())
b=sum(a)/len(a)
if b %int(b)==1:
    print(int(b))
else:
    print("%.2f"%b)

