a = eval(input())
b = eval(input())
c = []
c.append(a)
for i in range(b - 1):
    c.append(a)
    a = a/2
print("%.2f"%(sum(c)))



