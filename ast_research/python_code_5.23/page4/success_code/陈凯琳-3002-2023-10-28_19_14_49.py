lit=eval(input())
a=sum(lit)
b=a/len(lit)
if int(b)==b:
    print(int(b))
else:
    print("%.2f"%b)
