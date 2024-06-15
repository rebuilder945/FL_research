def work(a) :
    dic=dict()
    sum=1
    for i in range(0,a + 1):
        sum*=i+1
        dic.setdefault(i,sum)
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

