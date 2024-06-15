def work(a) :
dic={}
for x in range(a+1):
    dic[x]=math.factorial(x)
return dic
	

a = int(input())
ans = work(a)
print(ans)

