h=float(input())
N=int(input())
s=0
i=0
import math
while i<N:
    s=s+h*math.pow(1/2,i)
    i+=1
print("%.2f" % s)
