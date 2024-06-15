def work(a) :
    dic = {0:1}
    a = 1
    for i in range(1,n+1):
        a*=i
        dic[i] = a
    return dic
	

a = int(input())
ans = work(a)
print(ans)

