def work(a) :
    s={}
    b=1
    for x in range(0,a):
        b=b*(x+1)
        s[a]=b
    return s
	

a = int(input())
ans = work(a)
print(ans)

