import math

a,b = eval(input())
c,d = eval(input())
pf = (a-c)**2+(b-d)**2
dis = math.sqrt(pf)
print("%.2f"%(dis))
