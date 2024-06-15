def work(a) :
dict_temp = {}
for temp in range(num+1):
    dict_temp[temp] = math.factorial(temp)
	

a = int(input())
ans = work(a)
print(ans)

