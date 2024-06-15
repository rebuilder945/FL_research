def work(a) :
ans={}
b=1
for x in range(a):
    b=b*(x+1)
    ans[a]=b
return ans
	

a = int(input())
ans = work(a)
print(ans)

