import math
m = eval(input())
avg = sum(m)/len(m)
n = math.modf(avg)
if n[0] == 0:
    print("%d"%avg)
else:
    print("%.2f"%avg)
