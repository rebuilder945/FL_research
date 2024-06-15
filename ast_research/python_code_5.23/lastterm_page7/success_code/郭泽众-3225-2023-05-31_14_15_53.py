def work(a) :
    fac = 1
    dic = {0:1}
    for i in range(1, a+1):
        for j in range(1, i+1):
            fac = fac * j
        dic[i] = fac
        fac = 1
    return dic
	

a = int(input())
ans = work(a)
print(ans)

