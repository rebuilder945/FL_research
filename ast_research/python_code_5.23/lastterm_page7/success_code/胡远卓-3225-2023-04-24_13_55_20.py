def work(a) :
    dic={}
    tmp=1
    for i in range(a+1):
        dic[i]=tmp
        tmp*=(1+i)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

