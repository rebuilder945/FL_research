def work(a) :

    result=1
    dic={0:1}
    for i in range(1,a+1):
        result*=i
        dic[i]=result
    return dic
	

a = int(input())
ans = work(a)
print(ans)

