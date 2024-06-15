def work(a) :
import math
    dic={}
    for i in list(range(a+1)):
        b=math.factorial(i)
        dic[i]=b
    return dic
	

a = int(input())
ans = work(a)
print(ans)

