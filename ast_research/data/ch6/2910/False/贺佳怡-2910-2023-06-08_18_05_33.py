h=float(input())
N=int(input())
s=0
i=0
import math
while i<N:
    s=s+2*h*1/2  
    h=h/2
    i+=1
print("%.2f" % s)
