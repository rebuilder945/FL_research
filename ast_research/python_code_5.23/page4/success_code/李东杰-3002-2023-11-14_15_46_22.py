a=eval(input())
b=sum(a)/len(a)
if type(b)==float:
    print("%.2f"%b)
else:
    print(b)
