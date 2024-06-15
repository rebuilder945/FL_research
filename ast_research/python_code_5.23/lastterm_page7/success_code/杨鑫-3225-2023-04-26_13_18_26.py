def work(a) :
    b=1
    dic={0:1}
    for i in range(1,a+1):
        b=b*i
        dic[i]=b
    return dic
	

a = int(input())
ans = work(a)
print(ans)

