def work(a) :
    dic_num = {}
    for x in range(a+1):
        dic_num[x] = math.factorial(x)
    return dic_num
import math

	

a = int(input())
ans = work(a)
print(ans)

