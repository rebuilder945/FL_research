a = eval(input())
b = sum(a)/len(a)
if b.is_integer():
    print("%d"%b)
else:
    print("%.2f"%b)
