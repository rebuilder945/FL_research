def work(a) :
    dic={}
    for i in list(range(a+1)):
        b=math.factorial(i)
        dic[i]=b
    return dic
import math

	

a = int(input())
ans = work(a)
print(ans)

