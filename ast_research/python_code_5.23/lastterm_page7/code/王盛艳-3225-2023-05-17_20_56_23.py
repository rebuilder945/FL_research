def work(a) :
ans = {}
for i in range(a + 1):
    ans[i] = math.factorial(i)
	

a = int(input())
ans = work(a)
print(ans)

