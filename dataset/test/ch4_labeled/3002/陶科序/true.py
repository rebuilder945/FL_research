A = eval(input())
b = sum(A)
c = b/len(A)
d = int(c)
if c == d:
    print("%d"%c)
else:
    print("%.2f"%c)
