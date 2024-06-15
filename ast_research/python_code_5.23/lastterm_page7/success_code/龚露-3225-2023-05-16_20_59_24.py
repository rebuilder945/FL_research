def work(a) :
    def jiecheng(x):
        i = 1
        while i < x :
            b = x-1
            c = x*b
            b = b-1
            i = i + 1
        return c
    dic={}
    for x in range(a+1):
        dic[x]=dic.get(x,jiecheng(x))
    return dic
	

a = int(input())
ans = work(a)
print(ans)

