def work(a) :
    re={}
    b=1
    for i in range(a+1):
        if i > 0:
            b=b*i
        re[i]=b
    return re
	

a = int(input())
ans = work(a)
print(ans)

