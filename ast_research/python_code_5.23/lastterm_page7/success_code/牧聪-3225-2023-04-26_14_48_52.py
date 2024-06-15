def work(a) :
    if a==0:
        return {0:1}
    else:
        dic={}
        q=1
        for m in range (a+1):
            for n in range (m+1):
                q*=n
            dic[str(m)]=q
	

a = int(input())
ans = work(a)
print(ans)

