def work(a) :
  import math
  num = int(input())
  work = {}
  for i in range(num+1):
    work[i] = math.factorial(i)
print(work)
	

a = int(input())
ans = work(a)
print(ans)

