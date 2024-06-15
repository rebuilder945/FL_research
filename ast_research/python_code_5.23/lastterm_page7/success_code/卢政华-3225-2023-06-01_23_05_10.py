def work(a) :
    ans={}
    b=1
    for i in range(1,a+1):
          b=b*i
          ans[i]=b
    return ans
	

a = int(input())
ans = work(a)
print(ans)

