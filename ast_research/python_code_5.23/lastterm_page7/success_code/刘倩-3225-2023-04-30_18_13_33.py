def work(a) :
    dic = {}
    for x in range(0,a+1):
        if x == 0:
            dic[x] = 1
        else:
            dic[x] = dic[x+1]*x
    return dic
	

a = int(input())
ans = work(a)
print(ans)

