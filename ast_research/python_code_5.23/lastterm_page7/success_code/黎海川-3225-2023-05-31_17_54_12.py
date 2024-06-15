def work(a) :

    dic=dict()
    sum=1
    for i in range(1,a + 1):
        sum*=i
        dic=sum
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

