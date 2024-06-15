def work(a) :
    m = {0:1}
    ls=[]
    b=1
    for i in range(1,a+1):
        for j in range(1,i+1):
            b=b*j
        ls.append(b)
        b=1
        m[i]=ls[i-1]
    return m
	

a = int(input())
ans = work(a)
print(ans)

