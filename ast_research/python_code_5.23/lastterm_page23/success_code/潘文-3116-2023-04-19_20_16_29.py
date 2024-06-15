import math
from math import sqrt
m=input()
nls=m.split(",")
x1=eval(nls[0])
y1=eval(nls[1])
n=input()
nl=n.split(",")
x2=eval(nl[0])
y2=eval(nl[1])
r=sqrt(pow(x1-x2,2)+pow(y1-y2,2))
print("%.2f"%(r))
