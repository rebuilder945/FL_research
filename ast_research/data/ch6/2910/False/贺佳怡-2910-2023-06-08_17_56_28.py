h=float(input())
N=int(input())
s=0
i=0
import math
while i<N:
    s=s+h+2*h*math.pow(1/2,i+1)
    i+=1
print("%.2f" % s)
