import math
from statistics import mean
def pr(y):
    x=mean(y)
    z=math.floor(x);
    if(x==z):
        print("%.2f"%z)
    else:
        print("%.2f"%x)
sums=eval(input());
pr(sums)
