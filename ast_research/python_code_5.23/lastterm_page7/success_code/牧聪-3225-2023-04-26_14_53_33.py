def work(a) :
    if a==0:
        return {0:1}
    else:
        dic={}
        for m in range (a+1):
            q=1
            for n in range (1,m+1):
                q*=n
            dic[m]=q
        return dic

	

a = int(input())
ans = work(a)
print(ans)

