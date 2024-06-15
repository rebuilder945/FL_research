a = eval(input())
b = sum(a)/len(a)
if type(b) == int:
    print("%d"%b)
else:
    print("%.2f"%b)

