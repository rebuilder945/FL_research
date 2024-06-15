def work(a) :
    re={}
    b=1
    for i in range(1,a+1):
        b=b*i
        re[i]=b
    return re
	

a = int(input())
ans = work(a)
print(ans)

