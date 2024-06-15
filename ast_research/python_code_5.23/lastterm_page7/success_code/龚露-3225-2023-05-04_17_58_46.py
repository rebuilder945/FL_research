def work(a) :
    def jiecheng(x):
        i = 1
        while i < x :
            x = x*(x-1)
            i = i + 1
    return x
    dic={}
    for x in range(a+1):
        dic.get(x,jiecheng(x))
	

a = int(input())
ans = work(a)
print(ans)

