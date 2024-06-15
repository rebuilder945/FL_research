def work(a) :
    dict={}
        for i in range(a+1):
            dict[i]=fac(i)
    def fac(a):
        if a==0:
            return 1
        else:
            return a*fac(a-1)
	

a = int(input())
ans = work(a)
print(ans)

