def work(a) :
    dic = {}
    for x in range(0,a+1):
        for y in range(0,x):
            x = x*y
        dic[x] = x        
	

a = int(input())
ans = work(a)
print(ans)

