def work(a) :
    di_nums = {}
    for x in list(range(a+1)):
        di_nums[x] = math.factorial(x)
import math
	

a = int(input())
ans = work(a)
print(ans)

