def work(a) :
  ans = {0: 1}
  if a >= 1:
    for x in range(1,a + 1):
      s = 1
      for i in range(1,x + 1):
        s *= i
        ans[x] = s
  return ans

	

a = int(input())
ans = work(a)
print(ans)

