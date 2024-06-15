def work(a) :
    s={}
    b=0
    for x in range(a+1):
        b=b*x
        s[x]=b
    return s
	

a = int(input())
ans = work(a)
print(ans)

