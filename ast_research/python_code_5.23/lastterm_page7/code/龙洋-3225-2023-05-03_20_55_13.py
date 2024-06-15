def work(a) :
    i=1
    fine={}
    for x in range(a+1)：
        if x==0:
            fine[0]=1
        else:
            i=i*x
            fine[x]=i
    return fine

	

a = int(input())
ans = work(a)
print(ans)

