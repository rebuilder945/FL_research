def work(a) :
    s={}
    b=1
    for x in range(a+1):
        b=b*(x+1)
        s[x]=b
    return s
	

a = int(input())
ans = work(a)
print(ans)

