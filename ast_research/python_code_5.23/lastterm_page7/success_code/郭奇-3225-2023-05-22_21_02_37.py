def work(a) :
    def j(a):
        if a == 0:
            return 1
        else:
            return a*j(a-1)
    dic = {}   
    for i in range(a+1):
         dic[i]=j(i)
    return dic        
	

a = int(input())
ans = work(a)
print(ans)

