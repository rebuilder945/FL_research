def work(a) :
    ans={0:1}
    b=1
    for i in range(1,a+1):
          b=b*i
          ans[i]=b
    return ans
	

a = int(input())
ans = work(a)
print(ans)

