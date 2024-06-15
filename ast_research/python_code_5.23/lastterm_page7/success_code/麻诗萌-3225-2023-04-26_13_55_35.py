def work(a) :
    dic={}
    for i in range(a+1):
        m=1
        for x in range(1,i+1):
             m=m*x
        dic["i"]=m
    return ans
	

a = int(input())
ans = work(a)
print(ans)

