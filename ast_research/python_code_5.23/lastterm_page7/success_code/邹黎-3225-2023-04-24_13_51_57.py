def work(a) :

    dic={}
    y=1
    for x in range(0,a+1):
        if x!=0:
            y*=x
            dic[x]=y
        else:
            y=1
            dic[x]=y
    return dic
	

a = int(input())
ans = work(a)
print(ans)

