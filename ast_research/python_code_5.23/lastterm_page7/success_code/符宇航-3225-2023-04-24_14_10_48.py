def work(a) :
    dic={}
    for i in range(1,a+1):
        sum=1
        for x in range(1,i+1):
            sum=sum*x
        dic[i]=sum
    return dic

	

a = int(input())
ans = work(a)
print(ans)

