def work(a) :
    s={}
    b=1
    for x in range(a+1):
        if x=0:
            b=1
        else :
            b=b*x
        s[x]=b
    return s
	

a = int(input())
ans = work(a)
print(ans)

