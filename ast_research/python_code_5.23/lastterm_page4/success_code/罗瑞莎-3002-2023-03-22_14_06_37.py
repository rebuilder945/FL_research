import math
a = eval(input())
p = sum(a)/len(a)
b = math.modf(p)
if b[0] == 0:
    print("%d"%(p))
else:
    print("%.2f"%(p))
