def work(a) :
    ans={0:1}
    for i in range(1,a+1):
        ans[i]=ans.get(i-1)*i
    returnans
	

a = int(input())
ans = work(a)
print(ans)

