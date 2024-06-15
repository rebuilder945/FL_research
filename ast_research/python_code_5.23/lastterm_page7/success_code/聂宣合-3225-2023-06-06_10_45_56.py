def work(a) :
    dics={0:1}
    sum=1
    for i in range(1,a+1):
        sum*=i
        dics[i]=sum
    return dics
	

a = int(input())
ans = work(a)
print(ans)

