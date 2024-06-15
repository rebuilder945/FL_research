def work(a) :
    a  =  int(input())
    ans  =  work(a)
    print(ans)
import math
num = int(input())
dict_temp = {}
for temp in range(num+1):
    dict_temp[temp] = math.factorial(temp)
print(dict_temp)
	

a = int(input())
ans = work(a)
print(ans)

