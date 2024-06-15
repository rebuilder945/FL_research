def work(a) :

        di_nums={}
        for x in list(range(a+1)):
                di_nums[x]=math.factorial(x)
        return di_nums
import math
	

a = int(input())
ans = work(a)
print(ans)

