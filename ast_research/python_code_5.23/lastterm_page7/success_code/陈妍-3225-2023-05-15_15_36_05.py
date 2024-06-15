def work(a) :
         ans = {}
         for i in range(a+1):
                  temp = 1
                  for j in range(1,i+1):
                           temp = temp*j
                  ans[i] = temp
         return ans
	

a = int(input())
ans = work(a)
print(ans)

