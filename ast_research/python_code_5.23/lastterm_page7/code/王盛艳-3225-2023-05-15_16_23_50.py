def work(a) :
temp = {}
for i in range(a + 1):
    temp[i] = math.factorial(i)
	

a = int(input())
ans = work(a)
print(ans)

