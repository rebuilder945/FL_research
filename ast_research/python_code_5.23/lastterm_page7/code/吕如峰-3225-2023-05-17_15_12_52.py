def work(a) :
import math
num = int(input(）)
dict_temp = {}
for temp in range(num+1):
    dict_temp[temp] = math.factorial(temp)
return dict_temp
	

a = int(input())
ans = work(a)
print(ans)

