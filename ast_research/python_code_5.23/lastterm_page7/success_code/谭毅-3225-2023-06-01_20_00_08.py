def work(a) :
        di_nums={}
        fact=1
        for x in range(a+1):
                if x == 0:
                        fact = 1
                else:
                        fact *= x
        di_nums[x] = fact
        return di_nums
	

a = int(input())
ans = work(a)
print(ans)

