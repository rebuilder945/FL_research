def work(a) :
    def j(a):
        if a == 0:
            return 1
        else:
            return a*j(a-1)
    dic = {}   
    for i in range(a):
         dic[i]=j(a)
    return dic        
	

a = int(input())
ans = work(a)
print(ans)

