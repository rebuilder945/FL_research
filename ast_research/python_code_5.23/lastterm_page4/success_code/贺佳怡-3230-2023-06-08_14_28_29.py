a=eval(input())
a.sort(reverse=True)
b=len(a)
evn=0
import math
while b>0:
    evn=evn+a[0]*(math.pow(10,b-1))
    a.remove(a[0])
    b-=1
print(evn)

