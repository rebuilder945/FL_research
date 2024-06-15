def work(a) :
  import math
  work = {}
  for i in range(a+1):
    work[i] = math.factorial(i)
print(work)
	

a = int(input())
ans = work(a)
print(ans)

