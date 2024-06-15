def work(a) :
import math
d={}
for i in range(a):
    d['i']=math.factorial(i)
return d
	

a = int(input())
ans = work(a)
print(ans)

