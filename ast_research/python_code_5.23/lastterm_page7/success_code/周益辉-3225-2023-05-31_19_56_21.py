def work(a) :
    dic={}
    jie=1
    for m in range(a+1):
        for n in range(1,m+1):
            jie=jie*n
        dic[m]=jie
        jie=1
    return dic
	

a = int(input())
ans = work(a)
print(ans)

