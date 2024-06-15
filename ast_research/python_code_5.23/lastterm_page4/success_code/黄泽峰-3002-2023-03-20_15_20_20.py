from numpy import average


ls1 = eval(input())
x = average(ls1)
y = int(x)
if x==y:
    print("%d"%x)
else:
    print("%.2f"%x)

