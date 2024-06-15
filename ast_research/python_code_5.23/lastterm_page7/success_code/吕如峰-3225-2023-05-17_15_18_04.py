def work(a) :
  import math
  dict_temp = {}
  for temp in range(a+1):
     dict_temp[temp] = math.factorial(temp)
  return dict_temp
	

a = int(input())
ans = work(a)
print(ans)

