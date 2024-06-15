def work(a) :
    dic={}
    for i in range(a+1):
        dic[i]=i*i
    return dic
	

a = int(input())
ans = work(a)
print(ans)

