def work(a) :
    dic={}
    for i in range(0,a+1):
        b=a*i
        dic[a]=b
    return dic
	

a = int(input())
ans = work(a)
print(ans)

