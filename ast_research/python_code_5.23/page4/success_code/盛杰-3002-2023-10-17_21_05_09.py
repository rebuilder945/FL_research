ls=eval(input())
a=sum(ls)
b=a/len(ls)
if b%1==0:
    print(int(b))
else:
    print("%.2f"%b)

