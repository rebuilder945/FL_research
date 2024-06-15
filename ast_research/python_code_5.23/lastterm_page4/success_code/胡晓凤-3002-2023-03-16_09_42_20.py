import math
from statistics import mean
def avg(y):
    x=mean(y)
    z=math.floor(x)
    if(x==z):
        print(z)
    else:
        print("%.2f"%x)
sums=eval(input())
avg(sums)
