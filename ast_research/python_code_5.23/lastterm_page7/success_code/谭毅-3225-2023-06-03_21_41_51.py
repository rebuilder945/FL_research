def work(a) :
        di_nums={}
        fact=1
        ls=[]
        for x in range(a+1):
                if x == 0:
                        fact = 1
                else:
                        fact *= x
        ls[x] = fact
        di_nums[x]=ls[x]
        return di_nums
	

a = int(input())
ans = work(a)
print(ans)

