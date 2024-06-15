def work(a) :
        nums=set()
        for x in list(range(a+1)):
                nums[x]=math.factorial(x)
        return nums
import math
	

a = int(input())
ans = work(a)
print(ans)

