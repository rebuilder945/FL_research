h=float(input())
N=int(input())
s=0
i=0
import math
while i<N+1:
    h=h*1/2
    s=s+2*h
    i+=1
print("%.2f" % s)
