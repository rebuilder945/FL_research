def work(a) :
    b=1
    dic={0:1}
    for j in range(1,a+1):
        for i in range(1,j+1):
            b*=i
        dic[i]=b
        b=1
    return dic
	

a = int(input())
ans = work(a)
print(ans)

