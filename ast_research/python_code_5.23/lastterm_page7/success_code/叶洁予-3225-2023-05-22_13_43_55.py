def work(a) :
    ans={0:1}
    for i in range(1,a+1):
        ans[i]=ans.get(i-1)*i
    return ans

	

a = int(input())
ans = work(a)
print(ans)

