def work(a) :
        nums={}
        for x in list(range(a+1)):
                nums[x]=math.factorial(x)
        return nums
import math
	

a = int(input())
ans = work(a)
print(ans)

