a=input()
b=sum(a)/len(a)
if type(b)==int:
    print(b)
else:
    print("%.2f"%b)
