def work(a) :
    dic = {}
    for x in list(range(a+1)):
        dic[x] = math.factoral(x)
    return dic
import math
	

a = int(input())
ans = work(a)
print(ans)

