def work(a) :
res = {0:1}
fact = 1
for i in range(1, x+1):
    fact *= i
    res[i] = fact
return res
	

a = int(input())
ans = work(a)
print(ans)

