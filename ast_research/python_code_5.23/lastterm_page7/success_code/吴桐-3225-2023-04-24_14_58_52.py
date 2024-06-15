def work(a) :

    ans={}
    i=1
    j=1
    while i<=a+1:
        ans[str(i-1)]=j
        j*=i
        i+=1
    return ans
	

a = int(input())
ans = work(a)
print(ans)

