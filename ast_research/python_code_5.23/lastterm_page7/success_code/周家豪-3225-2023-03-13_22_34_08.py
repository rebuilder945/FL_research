def work(a) :
    dic={}
    for i in range(a+1):
        if i == 0:
            ji=1
            dic[i]=ji
        else:
            ji=1
            for x in range(1,i+1):
                ji=x*ji
            dic[i]=ji
    return dic
	

a = int(input())
ans = work(a)
print(ans)

